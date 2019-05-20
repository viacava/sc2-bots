import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

map_name = "Abyssal Reef LE"

class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration):
        if iteration == 0:
            for worker in self.workers:
                await self.do(worker.attack(self.enemy_start_locations[0]))

try:
    logging.info("run game in %s map", map_name)
    run_game(maps.get(map_name), [Bot(Race.Zerg, WorkerRushBot()),Computer(Race.Protoss, Difficulty.Medium)], realtime=True)
except FileNotFoundError as identifier:
    logging.critical(identifier)
