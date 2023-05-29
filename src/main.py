"""
Main bot executable file.
Copyright © 2023 Stepan Zubkov <stepanzubkov@florgon.com>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from vkbottle import Bot
from routes import labelers

import config

bot = Bot(token=config.VK_BOT_TOKEN)

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()
