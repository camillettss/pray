import imp
import os

import pyglet

from core.game import Game
from core.util import Box, yn

# Copyright (C) 2021 Francesco Camilletti

wide_range=(-4, 5)

do_wide = False #yn('do wide? ')

deletion_range = 10 if do_wide else 5

OFFSETS = []
for z in range(*wide_range):
    for y in range(*wide_range):
        for x in range(*wide_range):
            OFFSETS.append((x,y,z))

CLOSE_OFFSETS = []
for z in range(-1, 2):
    for y in range(-1, 2):
        for x in range(-1, 2):
            CLOSE_OFFSETS.append((x,y,z))
            OFFSETS.remove((x,y,z))

offset_information = Box(
    do_wide=do_wide,
    wide=OFFSETS,
    close=CLOSE_OFFSETS,
    deletion_range=deletion_range
)

if not os.path.isdir('worlds'):
    os.mkdir('worlds')

world = 'test'#input('Pick ur world: ')

if not world in os.listdir('worlds'):
    print('creating the world...')
    os.mkdir('worlds/'+world)
    gen_list = filter(lambda n: not n.startswith('_'),
                      [os.path.splitext(n)[0] for n in os.listdir('generators')]
                )
    print('Available generators:',', '.join(gen_list))
    generator = input('Select a generator: ')+'.py'
    open('worlds/'+world+'/generator','w').write(generator)
    generator = imp.load_source('generator', 'generators/'+generator)
    generator.initialize(world)
else:
    generator = imp.load_source('generator', 'generators/'+open('worlds/'+world+'/generator').read())

generator.load(world)

game = Game(world, generator, offset_information)
pyglet.app.run()
#asyncio.get_event_loop().run_forever()