from data_base import functions_for_create_objects
from data_base import functions_for_work_with_bd
from telegram.handlers import for_keyboard
from telegram.data.text_for_handlers import winner_text, looser_text
from aiogram.types import CallbackQuery
from logic import logic, phases
from classes import some_classes
from data_base.db import cursor, conn
from aiogram.utils.exceptions import MessageNotModified
import asyncio


async def start_game(t_id):
    # add to the data
    game = functions_for_create_objects.collect_current_game_from_in_queue()

    for player in (game.player_1, game.player_2):
        await for_keyboard.phase_place_ships(player)


async def call_back_for_phase_4(callback, game=False):
    t_id = callback.from_user.id
    if not game:
        game = functions_for_create_objects.collect_current_game_from_in_queue(t_id)

    turn_info = functions_for_work_with_bd.get_turn_info(game)  # [(turn, reverse_turn, cost_dict)]

    turn = turn_info[0]
    reverse_turn = turn_info[1]
    cost_dict_for_turn = turn_info[2]

    if t_id != cost_dict_for_turn[turn].t_id:
        print("noy you're turn")
        return

    player_for_hit = cost_dict_for_turn[reverse_turn]
    player = cost_dict_for_turn[turn]

    await call_back_for_hit(callback, player_for_hit, game)  # can change the turn in db if miss hit

    new_turn_info = functions_for_work_with_bd.get_turn_info(game)  # [(turn, reverse_turn, cost_dict)]

    new_turn = new_turn_info[0]
    new_reverse_turn = new_turn_info[1]
    new_cost_dict = new_turn_info[2]

    if turn != new_turn:
        print('sleep')
        await call_back_for_show_phase_4(callback, game, turn)
        await asyncio.sleep(1.5)

    await call_back_for_show_phase_4(callback, game)

    if logic.check_if_win(player_for_hit):
        # send for loser
        await for_keyboard.edit_message_after_someone_win(player=player_for_hit,
                                                          enemy_id=player.t_id,
                                                          function_for_text=looser_text)
        # send for winner
        await for_keyboard.edit_message_after_someone_win(player=player,
                                                          enemy_id=player_for_hit.t_id,
                                                          function_for_text=winner_text)

        functions_for_work_with_bd.clear_table_after_game(player.t_id)
        functions_for_work_with_bd.clear_table_after_game(player_for_hit.t_id)




async def call_back_for_hit(callback: CallbackQuery,
                            player_for_hit,
                            game: some_classes.SeaBattleGame = False, ):
    t_id = callback.from_user.id

    if not game:
        game = functions_for_create_objects.collect_current_game_from_in_queue(t_id)

    data = [int(cord) for cord in callback.data.split()]  # [y, x]
    y = data[0]
    x = data[1]

    if logic.hit(player=player_for_hit, y=y, x=x):  # if miss
        game.change_turn()


async def call_back_for_show_phase_4(callback: CallbackQuery,
                                     game=False,
                                     old_turn=False):
    turn_info = functions_for_work_with_bd.get_turn_info(game)  # [(turn, reverse_turn, cost_dict)]
    reverse_turn = turn_info[1]
    cost_dict_for_turn = turn_info[2]

    if old_turn and old_turn == reverse_turn:
        reverse_turn = turn_info[0]

    t_id = callback.from_user.id
    player_for_hit = cost_dict_for_turn[reverse_turn]
    # create game if it's none
    if not game:
        game = functions_for_create_objects.collect_current_game_from_in_queue(t_id)

    players = [game.player_1, game.player_2]

    for player in players:
        try:
            await for_keyboard.edit_message_after_hit(player, player_for_hit)
        except MessageNotModified:
            continue


async def call_back_for_phase_2(callback: CallbackQuery):
    t_id = callback.from_user.id
    game = functions_for_create_objects.collect_current_game_from_in_queue(callback.from_user.id)
    player = game.player_1 if game.player_1.t_id == t_id else game.player_2

    if callback.data == 'ready':
        functions_for_work_with_bd.change_phase(t_id=callback.from_user.id, phase=phases.phase_3)
        await for_keyboard.edit_message_after_ready(player)
        cursor.execute("SELECT player_phase FROM phase WHERE t_id = ? OR t_id = ?", (game.player_1.t_id,
                                                                                     game.player_2.t_id))
        phases_from_db = cursor.fetchall()  # [(),()]
        for phase in phases_from_db:
            if phase[0] != phases.phase_3:
                return

        functions_for_work_with_bd.change_phase(game.player_1.t_id, phases.phase_4)
        functions_for_work_with_bd.change_phase(game.player_2.t_id, phases.phase_4)

        await call_back_for_show_phase_4(callback, game)

    elif callback.data == 'random':
        await call_back_for_random(callback)

    else:
        await call_back_for_hit(callback, game)


async def call_back_for_random(callback: CallbackQuery):
    # check for free ships
    t_id = callback.from_user.id

    cursor.execute(f"SELECT * FROM ships WHERE t_id = {t_id}")
    tuple_with_basic_info_for_ships = cursor.fetchall()

    ships = functions_for_create_objects.create_ships(t_id, tuple_with_basic_info_for_ships)

    # create ships if all already placed
    for ship in ships:
        if not ship.already_place:
            break
        if ship.ship_id == '1.3':
            functions_for_create_objects.create_ships_for_random(t_id)

    game = functions_for_create_objects.collect_current_game_from_in_queue(t_id)

    player = game.player_1 if game.player_1.t_id == t_id else game.player_2

    logic.random_place(player)

    await for_keyboard.edit_message_after_random(player)
