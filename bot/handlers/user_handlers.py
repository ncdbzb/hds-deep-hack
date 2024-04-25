from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command, CommandStart, StateFilter
from bot.lexicon.lexicon_ru import LEXICON_RU
from bot.keyboards.keyboards import keyboard
from llm_agent.llm import get_answer

router = Router()


class FSMGame(StatesGroup):
    search_message = State()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/start'])
    await state.set_state(FSMGame.search_message)


@router.message(StateFilter(FSMGame.search_message))
async def process_llm_message(message: Message, state: FSMContext):
    response = get_answer(message.text)
    await message.answer(text=response)


# @router.callback_query(F.data == 'big_button_1_pressed')
# async def process_big_button_pressed(callback: CallbackQuery):
#     await callback.message.answer(text='нажамта кнопка')


