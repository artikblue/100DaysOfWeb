import quart
from services import starwars

blueprint = quart.blueprints.Blueprint(__name__, __name__)


@blueprint.route('/character/<n>', methods=['GET'])
async def character(n: str):
    character = await starwars.characters(n)

    return quart.jsonify(character)


@blueprint.route('/planet/<n>', methods=['GET'])
async def planet(n: str):
    planet = await starwars.planets(n)

    return quart.jsonify(planet)

@blueprint.route('/starship/<n>', methods=['GET'])
async def starship(n: str):
    starship = await starwars.starships(n)

    return quart.jsonify(starship)
