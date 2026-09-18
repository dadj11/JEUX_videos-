from config import (SCREEN_HIGHT,SCREEN_WITH)
import game

games = game.Game((SCREEN_WITH,SCREEN_HIGHT)," NOUVEAU JEUX")
games.run_loop()
