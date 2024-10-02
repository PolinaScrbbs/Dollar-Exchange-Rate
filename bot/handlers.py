from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import Form
from response import get_dollar_rate

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет, как вас зовут?")
    await state.set_state(Form.name)


@router.message(Form.name)
async def answer(message: Message, state: FSMContext):
    name = message.text
    rate = await get_dollar_rate()

    await message.answer(f"Рад знакомству, {name}! Курс доллара сегодня {rate}р")
    await state.clear()
