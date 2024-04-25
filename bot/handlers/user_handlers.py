from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command, CommandStart, StateFilter
from bot.lexicon.lexicon_ru import LEXICON_RU
from llm_agent.agent import Bibliography

router = Router()


class FSMGame(StatesGroup):
    search_message = State()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/start'])
    await state.set_state(FSMGame.search_message)


@router.message(StateFilter(FSMGame.search_message))
async def process_llm_message(message: Message):
    response = Bibliography(message.text).execute_agent()
    await message.answer(text=response)
