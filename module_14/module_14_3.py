from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb1 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
button = InlineKeyboardButton(text="Купить", callback_data="buy")
kb1.add(button1, button2, button)


kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text="Слива", callback_data="product_buying")
button4 = InlineKeyboardButton(text="Абрикос", callback_data="product_buying")
button5 = InlineKeyboardButton(text="Томат", callback_data="product_buying")
button6 = InlineKeyboardButton(text="Фруктовый сад", callback_data="product_buying")
kb2.add(button3, button4, button5, button6)


@dp.message_handler(commands='start')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb1)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("Формула для женщин: 10 x вес(кг) + 6,25 x рост(см) – 5 x возраст(г) – 161")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий составляет:{calories:.2f} ккал.")
    await state.finish()


@dp.callback_query_handler(text="buy")
async def get_buying_list(call):
    products = [
        ("Слива", "я слива лиловая, спелая, садовая", "слива.jpg", 11),
        ("Абрикос", "а я абрикос, на юге рос", "абрикос.jpg", 22),
        ("Томат", "а я томат", "помидор.jpg", 33),
        ("Фруктовый сад", "вместе мы фруктовый сад", "фруктовый_сад.jpg", 66)
    ]

    for name, description, image, price in products:
        with open(image, "rb") as img:
            await call.message.answer_photo(img)
        await call.message.answer(f"Название: '{name}' | Описание: '{description}' | Цена: {price}")
    await call.message.answer("Выберите продукт для покупки:", reply_markup=kb2)
    await call.answer()


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)