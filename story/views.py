from django.shortcuts import render
from .models import Stroy


# git commit -am "Backend accepting answers of questions & story is getting created" && git push

def male_story(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        x5 = request.POST.get('x5')
        x6 = request.POST.get('x6')
        x7 = request.POST.get('x7')
        x8 = request.POST.get('x8')
        x9 = request.POST.get('x9')
        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')
        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')
        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')
        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')
        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')
        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')
        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')
        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')
        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')
        x100 = request.POST.get('x100')
        x101 = request.POST.get('x101')
        x102 = request.POST.get('x102')
        x103 = request.POST.get('x103')
        x104 = request.POST.get('x104')
        x105 = request.POST.get('x105')
        x106 = request.POST.get('x106')
        x107 = request.POST.get('x107')
        x108 = request.POST.get('x108')
        x109 = request.POST.get('x109')
        x110 = request.POST.get('x110')
        x111 = request.POST.get('x111')
        x112 = request.POST.get('x112')
        x113 = request.POST.get('x113')
        x114 = request.POST.get('x114')
        x115 = request.POST.get('x115')
        x116 = request.POST.get('x116')
        x117 = request.POST.get('x117')
        x118 = request.POST.get('x118')
        x119 = request.POST.get('x119')
        x120 = request.POST.get('x120')
        x121 = request.POST.get('x121')
        x122 = request.POST.get('x122')
        x123 = request.POST.get('x123')
        x124 = request.POST.get('x124')
        x125 = request.POST.get('x125')
        x126 = request.POST.get('x126')
        x127 = request.POST.get('x127')
        x128 = request.POST.get('x128')
        x129 = request.POST.get('x129')
        x130 = request.POST.get('x130')
        x131 = request.POST.get('x131')
        x132 = request.POST.get('x132')
        x133 = request.POST.get('x133')
        x134 = request.POST.get('x134')
        x135 = request.POST.get('x135')
        x136 = request.POST.get('x136')
        x137 = request.POST.get('x137')
        x138 = request.POST.get('x138')
        x139 = request.POST.get('x139')
        x140 = request.POST.get('x140')
        x141 = request.POST.get('x141')
        x142 = request.POST.get('x142')
        x143 = request.POST.get('x143')
        x144 = request.POST.get('x144')
        x145 = request.POST.get('x145')
        x146 = request.POST.get('x146')
        x147 = request.POST.get('x147')
        x148 = request.POST.get('x148')
        x149 = request.POST.get('x149')
        x150 = request.POST.get('x150')
        x151 = request.POST.get('x151')
        x152 = request.POST.get('x152')
        x153 = request.POST.get('x153')
        x154 = request.POST.get('x154')
        x155 = request.POST.get('x155')
        x156 = request.POST.get('x156')
        x157 = request.POST.get('x157')
        x158 = request.POST.get('x158')
        x159 = request.POST.get('x159')
        x160 = request.POST.get('x160')
        x161 = request.POST.get('x161')
        x162 = request.POST.get('x162')
        x163 = request.POST.get('x163')
        x164 = request.POST.get('x164')
        x165 = request.POST.get('x165')
        x166 = request.POST.get('x166')
        x167 = request.POST.get('x167')
        x168 = request.POST.get('x168')
        x169 = request.POST.get('x169')
        x170 = request.POST.get('x170')
        x171 = request.POST.get('x171')
        x172 = request.POST.get('x172')
        x173 = request.POST.get('x173')
        x174 = request.POST.get('x174')
        x175 = request.POST.get('x175')
        x176 = request.POST.get('x176')
        x177 = request.POST.get('x177')
        x178 = request.POST.get('x178')
        x179 = request.POST.get('x179')
        x180 = request.POST.get('x180')
        x181 = request.POST.get('x181')
        x182 = request.POST.get('x182')
        x183 = request.POST.get('x183')
        x184 = request.POST.get('x184')
        x185 = request.POST.get('x185')
        x186 = request.POST.get('x186')
        x187 = request.POST.get('x187')
        x188 = request.POST.get('x188')
        x189 = request.POST.get('x189')
        x190 = request.POST.get('x190')
        x191 = request.POST.get('x191')
        x192 = request.POST.get('x192')
        x193 = request.POST.get('x193')
        x194 = request.POST.get('x194')
        x195 = request.POST.get('x195')
        x196 = request.POST.get('x196')
        x197 = request.POST.get('x197')
        x198 = request.POST.get('x198')
        x199 = request.POST.get('x199')
        x200 = request.POST.get('x200')
        x201 = request.POST.get('x201')
        x202 = request.POST.get('x202')
        x203 = request.POST.get('x203')
        x204 = request.POST.get('x204')
        x205 = request.POST.get('x205')
        x206 = request.POST.get('x206')
        x207 = request.POST.get('x207')
        x208 = request.POST.get('x208')
        x209 = request.POST.get('x209')
        x210 = request.POST.get('x210')
        x211 = request.POST.get('x211')
        x212 = request.POST.get('x212')
        x213 = request.POST.get('x213')
        x214 = request.POST.get('x214')
        x215 = request.POST.get('x215')
        x216 = request.POST.get('x216')
        x217 = request.POST.get('x217')
        x218 = request.POST.get('x218')
        x219 = request.POST.get('x219')
        x220 = request.POST.get('x220')
        x221 = request.POST.get('x221')
        x222 = request.POST.get('x222')
        x223 = request.POST.get('x223')
        x224 = request.POST.get('x224')
        x225 = request.POST.get('x225')
        x226 = request.POST.get('x226')
        x227 = request.POST.get('x227')
        x228 = request.POST.get('x228')
        x229 = request.POST.get('x229')
        x230 = request.POST.get('x230')
        x231 = request.POST.get('x231')
        x232 = request.POST.get('x232')
        x233 = request.POST.get('x233')
        x234 = request.POST.get('x234')
        x235 = request.POST.get('x235')
        x236 = request.POST.get('x236')
        x237 = request.POST.get('x237')
        x238 = request.POST.get('x238')
        x239 = request.POST.get('x239')
        x240 = request.POST.get('x240')
        x241 = request.POST.get('x241')
        x242 = request.POST.get('x242')
        x243 = request.POST.get('x243')
        x244 = request.POST.get('x244')
        x245 = request.POST.get('x245')
        x246 = request.POST.get('x246')
        x247 = request.POST.get('x247')
        x248 = request.POST.get('x248')
        x249 = request.POST.get('x249')
        x250 = request.POST.get('x250')
        x251 = request.POST.get('x251')
        x252 = request.POST.get('x252')
        x253 = request.POST.get('x253')
        x254 = request.POST.get('x254')
        x255 = request.POST.get('x255')
        x256 = request.POST.get('x256')
        x257 = request.POST.get('x257')
        x258 = request.POST.get('x258')
        x259 = request.POST.get('x259')
        x260 = request.POST.get('x260')
        x261 = request.POST.get('x261')
        x262 = request.POST.get('x262')
        x263 = request.POST.get('x263')
        x264 = request.POST.get('x264')
        x265 = request.POST.get('x265')
        x266 = request.POST.get('x266')
        x267 = request.POST.get('x267')
        x268 = request.POST.get('x268')
        x269 = request.POST.get('x269')
        x270 = request.POST.get('x270')
        x271 = request.POST.get('x271')
        x272 = request.POST.get('x272')
        x273 = request.POST.get('x273')
        x274 = request.POST.get('x274')
        x275 = request.POST.get('x275')
        x276 = request.POST.get('x276')
        x277 = request.POST.get('x277')
        x278 = request.POST.get('x278')
        x279 = request.POST.get('x279')
        x280 = request.POST.get('x280')
        x281 = request.POST.get('x281')
        x282 = request.POST.get('x282')
        x283 = request.POST.get('x283')
        x284 = request.POST.get('x284')
        x285 = request.POST.get('x285')
        x286 = request.POST.get('x286')
        x287 = request.POST.get('x287')
        x288 = request.POST.get('x288')
        x289 = request.POST.get('x289')
        x290 = request.POST.get('x290')
        x291 = request.POST.get('x291')
        x292 = request.POST.get('x292')
        x293 = request.POST.get('x293')
        x294 = request.POST.get('x294')
        x295 = request.POST.get('x295')
        x296 = request.POST.get('x296')
        x297 = request.POST.get('x297')
        x298 = request.POST.get('x298')
        x299 = request.POST.get('x299')
        x300 = request.POST.get('x300')
        x301 = request.POST.get('x301')
        x302 = request.POST.get('x302')
        x303 = request.POST.get('x303')
        x304 = request.POST.get('x304')
        x305 = request.POST.get('x305')
        x306 = request.POST.get('x306')
        x307 = request.POST.get('x307')
        x308 = request.POST.get('x308')
        x309 = request.POST.get('x309')
        x310 = request.POST.get('x310')
        x311 = request.POST.get('x311')
        x312 = request.POST.get('x312')
        x313 = request.POST.get('x313')
        x314 = request.POST.get('x314')
        x315 = request.POST.get('x315')
        x316 = request.POST.get('x316')
        x317 = request.POST.get('x317')
        x318 = request.POST.get('x318')
        x319 = request.POST.get('x319')
        x320 = request.POST.get('x320')
        x321 = request.POST.get('x321')
        x322 = request.POST.get('x322')
        x323 = request.POST.get('x323')
        x324 = request.POST.get('x324')
        x325 = request.POST.get('x325')
        x326 = request.POST.get('x326')
        x327 = request.POST.get('x327')
        x328 = request.POST.get('x328')
        x329 = request.POST.get('x329')
        x330 = request.POST.get('x330')
        x331 = request.POST.get('x331')
        x332 = request.POST.get('x332')
        x333 = request.POST.get('x333')
        x334 = request.POST.get('x334')
        x335 = request.POST.get('x335')
        x336 = request.POST.get('x336')
        x337 = request.POST.get('x337')
        x338 = request.POST.get('x338')
        x339 = request.POST.get('x339')
        x340 = request.POST.get('x340')
        x341 = request.POST.get('x341')
        x342 = request.POST.get('x342')
        x343 = request.POST.get('x343')
        x344 = request.POST.get('x344')
        x345 = request.POST.get('x345')
        x346 = request.POST.get('x346')
        x347 = request.POST.get('x347')
        x348 = request.POST.get('x348')
        x349 = request.POST.get('x349')
        x350 = request.POST.get('x350')
        x351 = request.POST.get('x351')
        x352 = request.POST.get('x352')
        x353 = request.POST.get('x353')
        x354 = request.POST.get('x354')
        x355 = request.POST.get('x355')
        x356 = request.POST.get('x356')
        x357 = request.POST.get('x357')
        x358 = request.POST.get('x358')
        x359 = request.POST.get('x359')
        x360 = request.POST.get('x360')
        x361 = request.POST.get('x361')
        x362 = request.POST.get('x362')
        x363 = request.POST.get('x363')
        x364 = request.POST.get('x364')
        x365 = request.POST.get('x365')
        x366 = request.POST.get('x366')
        x367 = request.POST.get('x367')
        x368 = request.POST.get('x368')
        x369 = request.POST.get('x369')
        x370 = request.POST.get('x370')
        x371 = request.POST.get('x371')
        x372 = request.POST.get('x372')
        x373 = request.POST.get('x373')
        x374 = request.POST.get('x374')
        x375 = request.POST.get('x375')
        x376 = request.POST.get('x376')
        x377 = request.POST.get('x377')
        x378 = request.POST.get('x378')
        x379 = request.POST.get('x379')
        x380 = request.POST.get('x380')
        x381 = request.POST.get('x381')
        x382 = request.POST.get('x382')
        x383 = request.POST.get('x383')
        x384 = request.POST.get('x384')
        x385 = request.POST.get('x385')
        x386 = request.POST.get('x386')
        x387 = request.POST.get('x387')
        x388 = request.POST.get('x388')
        x389 = request.POST.get('x389')
        x390 = request.POST.get('x390')
        x391 = request.POST.get('x391')
        x392 = request.POST.get('x392')
        x393 = request.POST.get('x393')
        x394 = request.POST.get('x394')
        x395 = request.POST.get('x395')
        x396 = request.POST.get('x396')
        x397 = request.POST.get('x397')
        x398 = request.POST.get('x398')
        x399 = request.POST.get('x399')
        x400 = request.POST.get('x400')
        x401 = request.POST.get('x401')
        x402 = request.POST.get('x402')
        x403 = request.POST.get('x403')
        x404 = request.POST.get('x404')
        x405 = request.POST.get('x405')
        x406 = request.POST.get('x406')
        x407 = request.POST.get('x407')
        x408 = request.POST.get('x408')
        x409 = request.POST.get('x409')
        x410 = request.POST.get('x410')
        x411 = request.POST.get('x411')
        x412 = request.POST.get('x412')
        x413 = request.POST.get('x413')
        x414 = request.POST.get('x414')
        x415 = request.POST.get('x415')
        x416 = request.POST.get('x416')
        x417 = request.POST.get('x417')
        x418 = request.POST.get('x418')
        x419 = request.POST.get('x419')
        x420 = request.POST.get('x420')
        x421 = request.POST.get('x421')
        x422 = request.POST.get('x422')
        x423 = request.POST.get('x423')
        x424 = request.POST.get('x424')
        x425 = request.POST.get('x425')
        x426 = request.POST.get('x426')
        x427 = request.POST.get('x427')
        x428 = request.POST.get('x428')
        x429 = request.POST.get('x429')
        x430 = request.POST.get('x430')
        x431 = request.POST.get('x431')
        x432 = request.POST.get('x432')
        x433 = request.POST.get('x433')
        x434 = request.POST.get('x434')
        x435 = request.POST.get('x435')
        x436 = request.POST.get('x436')
        x437 = request.POST.get('x437')
        x438 = request.POST.get('x438')
        x439 = request.POST.get('x439')
        x440 = request.POST.get('x440')
        x441 = request.POST.get('x441')
        x442 = request.POST.get('x442')
        x443 = request.POST.get('x443')
        x444 = request.POST.get('x444')
        x445 = request.POST.get('x445')
        x446 = request.POST.get('x446')
        x447 = request.POST.get('x447')
        x448 = request.POST.get('x448')
        x449 = request.POST.get('x449')
        x450 = request.POST.get('x450')
        x451 = request.POST.get('x451')
        x452 = request.POST.get('x452')
        x453 = request.POST.get('x453')
        x454 = request.POST.get('x454')
        x455 = request.POST.get('x455')
        x456 = request.POST.get('x456')
        x457 = request.POST.get('x457')
        x458 = request.POST.get('x458')
        x459 = request.POST.get('x459')
        x460 = request.POST.get('x460')
        x461 = request.POST.get('x461')
        x462 = request.POST.get('x462')
        x463 = request.POST.get('x463')
        x464 = request.POST.get('x464')
        x465 = request.POST.get('x465')
        x466 = request.POST.get('x466')
        x467 = request.POST.get('x467')
        x468 = request.POST.get('x468')
        x469 = request.POST.get('x469')
        x470 = request.POST.get('x470')
        x471 = request.POST.get('x471')
        x472 = request.POST.get('x472')
        x473 = request.POST.get('x473')
        x474 = request.POST.get('x474')
        x475 = request.POST.get('x475')
        x476 = request.POST.get('x476')
        x477 = request.POST.get('x477')
        x478 = request.POST.get('x478')
        x479 = request.POST.get('x479')
        x480 = request.POST.get('x480')
        x481 = request.POST.get('x481')
        x482 = request.POST.get('x482')
        x483 = request.POST.get('x483')
        x484 = request.POST.get('x484')
        x485 = request.POST.get('x485')
        x486 = request.POST.get('x486')
        x487 = request.POST.get('x487')
        x488 = request.POST.get('x488')
        x489 = request.POST.get('x489')
        x490 = request.POST.get('x490')
        x491 = request.POST.get('x491')
        x492 = request.POST.get('x492')
        x493 = request.POST.get('x493')
        x494 = request.POST.get('x494')
        x495 = request.POST.get('x495')
        x496 = request.POST.get('x496')
        x497 = request.POST.get('x497')
        x498 = request.POST.get('x498')
        x499 = request.POST.get('x499')
        x500 = request.POST.get('x500')
        x501 = request.POST.get('x501')
        x502 = request.POST.get('x502')
        x503 = request.POST.get('x503')
        x504 = request.POST.get('x504')
        x505 = request.POST.get('x505')
        x506 = request.POST.get('x506')
        x507 = request.POST.get('x507')
        x508 = request.POST.get('x508')
        x509 = request.POST.get('x509')
        x510 = request.POST.get('x510')
        x511 = request.POST.get('x511')
        x512 = request.POST.get('x512')
        x513 = request.POST.get('x513')
        x514 = request.POST.get('x514')
        x515 = request.POST.get('x515')
        x516 = request.POST.get('x516')
        x517 = request.POST.get('x517')
        x518 = request.POST.get('x518')
        x519 = request.POST.get('x519')
        x520 = request.POST.get('x520')
        x521 = request.POST.get('x521')
        x522 = request.POST.get('x522')
        x523 = request.POST.get('x523')
        x524 = request.POST.get('x524')
        x525 = request.POST.get('x525')
        x526 = request.POST.get('x526')
        x527 = request.POST.get('x527')
        x528 = request.POST.get('x528')
        x529 = request.POST.get('x529')
        x530 = request.POST.get('x530')
        x531 = request.POST.get('x531')
        x532 = request.POST.get('x532')
        x533 = request.POST.get('x533')
        x534 = request.POST.get('x534')
        x535 = request.POST.get('x535')
        x536 = request.POST.get('x536')
        x537 = request.POST.get('x537')
        x538 = request.POST.get('x538')
        x539 = request.POST.get('x539')
        x540 = request.POST.get('x540')
        x541 = request.POST.get('x541')
        x542 = request.POST.get('x542')
        x543 = request.POST.get('x543')
        x544 = request.POST.get('x544')
        x545 = request.POST.get('x545')
        x546 = request.POST.get('x546')
        x547 = request.POST.get('x547')
        x548 = request.POST.get('x548')
        x549 = request.POST.get('x549')
        x550 = request.POST.get('x550')
        x551 = request.POST.get('x551')
        x552 = request.POST.get('x552')
        x553 = request.POST.get('x553')
        x554 = request.POST.get('x554')
        x555 = request.POST.get('x555')
        x556 = request.POST.get('x556')
        x557 = request.POST.get('x557')
        x558 = request.POST.get('x558')
        x559 = request.POST.get('x559')
        x560 = request.POST.get('x560')
        x561 = request.POST.get('x561')
        x562 = request.POST.get('x562')
        x563 = request.POST.get('x563')
        x564 = request.POST.get('x564')
        x565 = request.POST.get('x565')
        x566 = request.POST.get('x566')
        x567 = request.POST.get('x567')
        x568 = request.POST.get('x568')
        x569 = request.POST.get('x569')
        x570 = request.POST.get('x570')
        x571 = request.POST.get('x571')
        x572 = request.POST.get('x572')
        x580 = request.POST.get('x580')
        x581 = request.POST.get('x581')
        male = f"""I was born on the {x1} in {x2}, a city in {x3} at {x4} hospital.
            My full name is {x5} .

            The people who decided on this name are {x6}.
            I was named this way because {x7}.Sometimes, I go by the nickname {x8} which I got from {x9}.
            I have a beautiful mother named {x10}. She was born on {x11} in {x12}.
            The place she grew up in {x13} was lovely just like her.
            Meanwhile, my father, {x14}, was born on the {x15}. He was raised in
            the city of {x16}.


            To complete my family, I have {x17} siblings.
            Their names are {x18}. They were born in {x19}. My mother gave birth
            to {20} on {x21}. On the other hand,
            {x22} was born on {x23}.
            I have a beautiful/handsome sister/brother who goes by the name {x24}. She/he was born on the
            {x25} in
            {x26}.
            My mother was raised well by her parents, {x7} and {x27}. My
            grandmother was named {x28}. Her birthday was on
            the {x29}; whereas, my grandpa, {x30}, was born on {x31} in the village of {x32}.


            On my father???s side, I was blessed with the lives of my grandma, {x33}, and my grandpa, {x34}.
            Granny was born on {x35} in {x36}. My grandfather???s birth date,
            however, was on {x37}. His family
            gleefully welcomed him on this day in the city of {x38}.



            I have the most gorgeous wife. She was named {x39} but I call her {x40}. I am thankful that she was successfully given
            birth to on the{x41} in the wonderful city of {x42}.

            {x43} and I were blessed with {x44} children who we named as {x45}.
            {x46} was born on {x47} in {x48}. On the
            other hand, {x49}???s birthdate is on {x50}. My wife gave
            birth to him/her in {x51}.



            Over the years, my children grew up and had their own kids, too. My adorable grandkids are named {x580} and {x581}.
            The first one is born in {x52} on the {x53}.
            {x54} was born on {x55} in the city of {x55}.



            I spend most of my free time {x56} while drinking {x57}.


            My most favorite sport is {x58} because I think it is {x59}


            My go-to vacation spot is {x61}. I find it {x62}.


            The meal that I enjoy the most is {x63}.


            My favorite song is called {x64}; it is sung by {x65}. The reason why
            I love it is that it reminds me of
            {x67}.


            Currently, my favorite television show is {x68}. Back then, I really loved the series {x69}.



            I have watched the movie {x70} several times already and I never get tired of it because it is
            {x71}.


            My hobbies are {x72}, {x73}, and {x74}. On
            the weekends, I also {x75} with my {x76}.



            The social gatherings that I usually enjoy are {x77}.


            My greatest talent is {x78}. I have used it in many ways throughout my life such as when I
            {x79}.


            The best characteristic that I love about myself is my {x80}.

            Sometimes, I wish I could stop being {x81}.



            Currently, I am living a {x81} life here in {x82} with my {x83}.
            On the weekdays, I spend most of my time {x84}. By the end of the day, I would feel {x85} and {x86}.



            I grew up in a {x87} neighborhood where I met various interesting people like {x88}.
            Remembering it, I can say that it was actually a {x89} place.


            My childhood home was {x90}. I enjoyed all of the {x91} mornings and
            {x92} nights in it. The house was
            suitable for a family of {x93} people. My time there was {x94}.



            My favorite place in this {x95} house was the {x96}. It had a special
            place in my heart because it {x97}.




            When I was younger, I had to do chores like {x98}.


            ({x99}) I got a daily/weekly/monthly allowance worth {x100}.



            The indoor activity that I enjoyed the most was {x101}. This was because {x102}.


            Back then, I really enjoyed {x103} outside the house.


            As a child, I was particularly skilled at {x104}.



            I also had some toys that cheered me up on sad days. These are {x105}.



            I had a special place that I called ???mine.??? It was this {x106} space filled with {x107}. I used to {x108} a lot when
            I stayed here.


            As a child, I always anticipated going out to {x109}.



            Being a boy, I {x110} not enjoy reading.
            (If yes) I liked collecting {x111} books!


            of this experience???{x112}
            I lived in a {x113} (Religious/Non-Religious) family.
            (If religious). I attended a church called {x114} which was located in {x115}. I remember the times when I {x116}.

            I {x117} baptized or dedicated as an infant.
            (If baptized) As an infant, I was baptized by {x118} in {x119}. My
            {x120} attended the celebration



            Some of the childhood experiences that helped me become who I am right now are {x121}.



            I remember having a childhood friend named {x122}. He/she was very {x123} and we had a {x124} time together.



            From my childhood, I will be eternally grateful for the {x125}. Because of it, I grew up to be
            a {x126} person.
            Family LIFE
            50 A family is a circle of love?????formed by memories,??filled with devotion.????



            My favorite memory with my dad was when {x127}. This is a special event for me because {x128}.



            My father???s insights on life and its adventures was {x129}. This made me become more {x130} regarding my own life.


            My father and I used to {x131} together and I really enjoyed it because {x132}.


            I think I have grown up to be like my father when it comes to my {x133}. I always think that I
            got this from him.


            One thing my dad always said was {x134}. I believe that this is actually a great {x135} and it helped me
            establish myself.


            My father worked as a/an {x136}. This job piqued / did not pique my interest because {x137}.


            One of the most memorable things about my mother from when I was a little boy was how she {x138}. This is because {x139}.

            My mom always had a {x140} outlook towards life. This attitude of hers affected me in a way
            that I became more {x141}.



            I am similar to her because she is {x142} just like me. My mother is the most {x143} woman I have ever met and I love her
            for it.


            Back when I was a child, I really liked {x144} with my mom. Until now, I still feel {x145} whenever I remember this.




            My mother???s occupation was {x146}. This helped me decide on my future career because I found it
            {x147} how she
            {x148}.


            My family was {x149}. We encountered problems such as {x150} and it
            was hard for me growing up. But
            I am now {x151} about my life. These circumstances have made me {x152}
            and {x153}.

            As I was growing up, my parents requested that I {x154}.


            This formed my mindset regarding parenting. In complete honesty, I actually require my children to {x155}, similar to /
            different from the obligations I had as a kid.


            Some of the qualities that my parents nurtured in me are my characteristics of being {x156} and
            {x157}. I am thankful for these.



            My parents always told me to be a {x158} person. Of course, I valued their encouragement
            because I loved them.



            I also loved my siblings/sister/brother so much. My fondest memories of them/him/her was that time when {x159}.

            Of course, being young means you get to enjoy the beauty of life without heavily thinking of the consequences. I played
            around with my
            siblings/brother/sister and we used to {x160}. It was funny for me back then but looking back,
            I think {x161}.
            My siblings/brother/sister and I were {x162}. We had {x163} days
            together.
            In addition to our lovely family, we had a pet {x164} / pets named {x165}. He/she/they were adorable!
            The thing I loved most about having {x166} growing up with me was {x167}. I loved {x168} with {x169}!
            On regular days, my family {x170} together. In the summer, we would often go {x171}. But most especially,
            we loved spending time together, either by {x172} or {x173}.
            My early memories of my grandparents was how they {x174}. My grandma would always {x175} while my grandpa {x176}.

            They lived in a lovely place in {x177}. Around their area, there were many {x178}. It was a {x179} neighborhood.
            My grandmother worked as a {x180} and my grandpa did some {x181} job.

            Whenever my family visited them / whenever they visited us, I remember that we always had an amazing time together. My
            grandma and
            grandpa prepares a delicious meal for us. Their {x182} was my favorite!

            I loved being with my grandparents because they were {x183}. I always watched them {x184} . They cared for me and my
            siblings/brother/sister.
            A valuable lesson that I learned from being with them was that {x185}. Aside from this, I was
            also inspired by them to be a {x186}
            person.
            The only things I remember about my great-grandparents are that they {x187}.
            I believe that my ancestors were {x188} and that I might have a/an {x189} origin.
            My favorite home-cooked meal was {x190} because it was honestly delicious and {x191}! It reminds me of {x192}.
            Whenever my family and I {x193} together, we would always prepare {x194}.
            We used to go out for dinner frequently/sometimes. When we do, I would always request that we go to {x195} or try other restaurants
            that serve {x196}.
            (Yes) Our house was a great place for celebrations. I remember having company often. My family???s friends or some of our
            other relatives
            would always come to visit or {x197} with us.
            (No) Although we were a happy family, we did not often have company perhaps because our place was {x198}.
            My family outings were {x199}! We would always go to {x200} and {x201} together. Holidays are my {x202} favorite season!
            In the winter, I remember {x203} with my siblings/brother/sister. As a whole family, we liked
            playing {x204}. My favorite
            winter food was {x205}. And drinks? Of course, {x206}.
            Family reunions are {x207} for me. I enjoyed {x208} whenever we held
            one.
            (No) I was not really close to my relatives.
            (Yes) I had close relationships with my other relatives especially with my {x209}. I am happy
            about these because I could always
            {x210} to them whenever I am {x211}.

            Every time I think about my family, the first thing that comes to mind was {x212}. I feel like
            I associated them with it because of
            the {x213} they bring to my life.

            Knowledge is the power??that gives us wings to soar.??

            I attended elementary at {x214} in {x215}. I often rode the {x216} to school and back OR I often biked/walked to
            school alone/with my {x217}.My earliest memories of going to {x218} was that I would always {x219}
            in {x220} Class. I also remember hanging out
            with my childhood friends named {x221} and {x222}.
            92 WHAT DID YOU ENJOY?? MOST ABOUT ELEMENTARY SCHOOL?????
            One thing I loved most about elementary was {x223} on {x224} days.
            But, I really hated that I had to {x225}.
            Next, I attended middle school at {x226}. Every day, I would go there via {x227}. Sometimes, I would {x228}.
            When I was in high school, I attended {x229}. It was a very {x230}
            school and I met a lot of {x231} people there.
            My favorite subjects in middle school were {x232} and {x233} because
            {x234}.
            Meanwhile, in high school, I really liked going to {x235} class. The teacher was really {x236} and my classmates were
            {x237}.
            Some extracurricular activities that I enjoyed the most were {x238}. I chose these because
            {x239}.
            Over the years, I have received some special awards such as {x240}.
            I had a favorite teacher whose name was {x241}. I can say that she/he had a big influence on
            shaping who I am now by {x242}.
            Back when I was still in school, there were many fashion trends that arose such as {x243}.
            (Yes) I participated in them because {x244}.
            (No) I did not participate much when it comes to these because {x245}.
            The most popular songs that I remember around the time I was studying were {x246}. I really
            {x247} this kind of music.
            Meanwhile, the highest grossing movies were {x248}. People {x249}
            these so much!
            The television shows that were much awaited were {x250}.
            Lastly, celebrities such as {x251} were having their primes then.
            The parties that I attended were mostly {x252}. Some of the party-goers were from {x253}. I can still remember
            how {x254} the crowd was.
            (No) I didn???t have a car when I was in high school but if I did it probably would be a __________.
            (Yes) I had a car when I was a teenager and it was a {x255}. I was {x256} about how it looks like.
            I really went places with that car.
            My middle school and high school years were a bit difficult because of {x257}. But, as a whole
            I think I really {x258}
            my teenage years.
            DURING YOUR MIDDLE SCHOOL AND HIGH SCHOOL YEARS???
            I am happy that I got to {x259} while I was schooling. It was a great privilege for me.
            change with time?????
            During this time, I was thinking about my goal of becoming a {x260} and I really hoped to
            achieve my dreams such as
            that of {x261}. Over time, I continued/stopped inching towards these goals.
            After graduation, I chose to follow the path of becoming a {x262}.
            I went to college / a career training school called {x263} in the city of {x264}. I took up a degree in the field of
            {x265}.
            I had to move away from home to continue studying and it was {x266}. I was looking forward to
            {x267} but I really felt
            {x268} when I was away from my family.
            I lived in an apartment/dorm nearby. It was {x269}, {x270}, and {x271}. I had a {x272} time studying when I was
            there.
            (with roommate) I had a roommate whose name was {x273}. He/she was a {x274} person.
            My most favorite college memories were the one at {x275} with my {x276}. Those experiences were {x277}
            and unforgettable.
            On??the Job??

            Any job can be made great.??It???s the worker???not the work?????that counts

            When I was young, I tried to gain money by {x278}. My earnings were used to pay for my {x279}.


            My first career-oriented job after graduation was a {x280} at {x281}.
            Here, I would be the one responsible for
            {x282}.
            When I found out that I got accepted in this job, I was very {x283}. I thought that this can
            help me in {x284}.
            The one thing I love most about my first job was {x285}. The environment in the workplace was
            also {x286}.
            Among the jobs that I tried and had in the past, the one in which I probably had the most fun was when I was working at
            {x287}
            as a {x288}. This is due to the fact that {x289}.

            Meanwhile, the worst job was in {x290}. I mostly did not enjoy working here because of {x291}.
            The most rewarding out of all, however, was the job at {x292}. This is because I was {x293}. I really love
            {x294} about this job.
            Of course, some opportunities can only be achieved when you move out of your comfort zone. As for me, I had to move away
            when I
            was working at {x295} in {x296}. I felt {x297} because of it but I am {x298} that I took it.
            For some jobs, I had to go places for {x299} events. The most memorable place I visited while
            doing so was a {x300} in {x301}.
            I had a coworker / superior who displayed the role of a friendly and trustworthy mentor to me. His/her name was {x302} and
            he/she taught me how to {x303}.
            (If yes) Over the years, I was able to be a mentor to others, too. I believe it was a {x304}
            experience for me.
            (If no) I might not have been an official mentor to others myself, but I believe that I was also able to help my
            colleagues in various ways.

            At work, I met all types of people but I found {x305} friends, too.
            When I???m just at home, I like to work on {x306}.
            But, I usually avoid doing {x307} because {x308}.
            Love??AND??Marriage????
            130 When love touches our hearts,??happiness fills our days.??

            I remember having a crush on {x309} when I was younger. I believe she was the first person I
            truly admired.
            The first boy party that I attended was when I was {x310} years old. It was held at {x311}..
            My first kiss was {x312}. I remember how I felt really {x313}
            afterwards.
            My first ever date was {x314}. It went {x315}. I had a {x316} time with {x317}.
            When that happened, lovers usually {x318} when they went out together and hung out. The kind of
            date nights was very {x319}
            compared to now.
            I met my lovely wife when I was {x320} years old.


            I will be eternally grateful that our paths crossed on {x321} in {x322}. If it weren???t for the {x323},
            I wouldn???t have seen her.
            She was {x324}, {x325}, and {x326}. Those
            qualities really captured my attention.
            Initially, I thought that she was {x327}. Over time, I realized how {x328} my first impression was compared to how
            she really is.
            I courted her for {x329} months. She was definitely worth the wait.
            When we just started dating, we really loved {x330} together. Some other things that we enjoyed
            doing were {x331}
            and {x332}.
            I knew she was the one when {x333} after I realized that she could be {x334}.
            The marriage proposal was {x335} and I am sincerely {x336} about it!
            There were {x337} everywhere while I
            was waiting for her response.
            We officially tied the knot on {x338} at a {x339} in {x340}.


            I wore a {x341}.

            While she wore a beautiful and {x342} wedding dress/gown.??

            It was a small/big wedding. We had about {x343} guests.

            For our first dance as husband and wife, we swayed to the song entitled {x344} which was chosen
            because {x345}.
            The most remarkable memory of mine from that special day was {x346}.

            Recall a special moment or event from the honeymoon.??
            Our honeymoon was {x347}! We went to {x348} wherein we {x349}. What I loved most about this
            experience was the fact that {x350}.


            After getting married, we lived in {x351}. I clearly remember how {x352} our home was.


            Early into our marriage, we had {x353} nights where we would enjoy dinner together over a
            {x354}.
            We started thinking about having children when {x355}. I really looked forward to {x356} and seeing my wife
            {x357} for our kids.


            WHEN YOU WERE FIRST MARRIED???What were some of the fun things you did with them???
            As a couple, we had some close friends. The ones that we mostly hung out with were named {x358}.
            We would always {x359} together and it felt {x360}! I {x361} spending time with them.


            {x362} and I really loved {x363} whenever we had free time. Aside from
            this, we also enjoyed {x364}.
            For me, marriage has been rewarding because {x365}.
            To be able to withstand any hardship, I believe that the most important key to a healthy marriage is {x366}.
            Of course in our marriage we also had hard times wherein we needed to be there for each other more. These instances that
            required
            sharing and companionship happened when {x367}.
            My daily relationship with my loving wife has been {x368}. Right now, my favorite thing about
            being married to is {x369}.
            Parenting????
            To be a father is to protect,??nurture, and guide,??but most of all, to love.????


            When I found out that I was going to be a dad, I felt {x370}. I remember that day being a
            {x371}
            one.
            I lived in {x372}
            My FIRST CHILD WAS BORN on ??{x373}
            My growing family then lived at a {x374} in {x375}.


            Back then, our situation was {x376}.
            We had problems such as {x377} OR We did not have any problems.


            Every time I looked at my firstborn when he/she was an infant, I felt {x378}. Every day with
            him/her was really
            {x379}.


            Becoming a father was {x380}. It caused me to have a more {x381}
            outlook on life. I realized that {x382}.
            168 WHAT IS YOUR MOST VIVID MEMORY??OF YOUR CHILDREN???S EARLY YEARS?????
            I have some crystal clear memories of my children when they were still young. These include the time when {x383} and
            also that instance when {x384}.


            Back then, I really enjoyed {x386} with them. When they grew up a bit, we would always {x385}.
            Of course, there had to be some days that I would need to spend alone with my wife. Whenever we took the days off for
            our special dates,
            we would {x387}.

            As a parent, I believe that it is undeniable that I have similarities with my kids. These include {x388}.
            As for them, my kids are similar in a way that they are all {x389}. This might be because
            {x390}.
            My spouse and I tried to instill the qualities of being {x391}, {x392}, and {x393} to our kids.
            I know that I have been blessed to be a father because I get to experience {x394}. This is what
            I consider my greatest joy
            in this {x395} role.
            Because life is not perfect, our family had problems, too. The greatest challenge that I experienced as a dad to {x396} beautiful kids
            was {x397}.
            I was raised in a {x398} family which is similar/different to my children???s upbringing. They
            grew up in a {x399} house, a
            {x400} neighborhood, with {x401} parents.
            THAT YOU WISH YOU???D KNOWN WHEN YOU??FIRST BECAME A FATHER?????
            Sometimes, I wish that I knew better when I became a father to my firstborn. One thing that I learned through time that
            I could
            have known back when I was raising {x402} was {x403}.
            I am a {x404} person. Somehow I wish my kids can grow up to be {x405}
            -- opposite/similar to me.
            Being a father taught me a lot of {x406} lessons but to me the most important thing among all
            these is {x407}.
            This is due to the fact that {x408}.


            Life offers so many??wonderful things to share,??so many special joys to celebrate.????

            We would always {x409} on my birthday when I was young. The guests were usually {x410}. It was a {x411}
            celebration.


            My favorite memory of a birthday party was when {x412}. This happened on my {x413} th birthday.
            The most special presents that I ever received are {x414}. For me, they were wonderful because
            {x415}.
            I often requested that my parents cook/make/buy {x416} to serve on my birthdays. I really loved
            these food because
            {x417}.
            Apart from the celebration of my birth, I had other unique parties held at our humble abode. These include {x418}.
            The ambiance of the surroundings during this feast was {x419}. Guests had to wear {x420}.
            As a child, my favorite religious festivity is {x421}. We would {x422}
            together as a family and {x423}.
            We prepare meals such as {x424} to feast on.
            Among these types of celebrations, the main thing that stands out in my memory is {x425} due to
            the fact that
            {x426}.

            I really liked the {x427} that we buy/make during my childhood. It tasted {x428} and {x429}.
            My favorite christmas carol was {x420}. Right now, {x431} is my
            favorite.
            where??it??came??from?????
            What my family told us about Santa Claus was that he was/wasn???t real. I always knew/didn???t know where the gifts from my
            Christmas
            stocking / ornament came from.
            During these holidays, we often gave presents to each other. My most loved gift was the {x432}
            from my {x433}
            because {x434}.
            Meanwhile, the most memorable present that I gave someone was a {x435}. This was for my {x436}.
            I still remember how he/she {x437} it.
            Growing up, I always loved the religious tradition we had in our family. Now that I have my own, I continued to {x438}.
            As a parent, the most meaningful Christmas for me was when {x439} because {x440}.
            195 HOW DID YOU CELEBRATE THANKSGIVING???Did you have a favourite Thanksgiving tradition?????
            For Thanksgiving, my family usually {x441}. The tradition that I love most is {x442}.
            Preparing and eating Thanksgiving food is also {x443}.
            When I was a kid, I really {x444} Australia day. The neighborhood would always be {x445} and there were {x446}
            everywhere!
            What was your favourite Halloween treat?????
            I did/didn???t really enjoy halloween. I remember an especially fun costume worn by {x447}. It
            was a {x448}.
            I also {x449} to trick-or-treat! My favorite treat was {x450} since
            {x451}. One memory that I have of a really enjoyable holiday celebration was when {x452}. It happened around the time that {x453}. I think it was a meaningful experience for me because {x454}.
            Moment by moment,??day by day,??families create a lifetime of memories.??The happiest time of my life, I must say, is when {x455}. I cannot explain the joy that I felt because {x456}. To me, it???s an experience that cannot be beaten by anything else. Meanwhile, the saddest for me was when {x457}. I believe I had a {x458} time moving on from this
            because {x459}. Over the years, I had many commitments and responsibilities but there was a time wherein I was always occupied.
            The busiest I have ever been was when {x460}. It was due to the fact that {x461}. On the other hand, I had relaxing days, too, but I am confident to say that I was most comfortable and at ease when
            {x462}. A life-changing event that really influenced me in many ways was when {x463}. Somehow, it
            helped me {x464}. One political event that I participated in or witnessed over the years was {x465}. It made a
            really strong impression on for the reason that {x466}.  (I have) I served in the military back then. It was a {x467} experience, while at the same
            time, there were instances that {x468} me such as {x469}. (Other family members have) Some of my relatives had to serve in the military. I was really {x470} about it and it
            often {x471} me thinking about what was happening to them while in there.
            I can proudly say that I was able to {x472}. This had been fulfilling for me because {x473}.
            I have been in an accident/major surgery/long illness. This involved me being {x474}.
            It sincerely didn???t have / had a lasting effect on me because it made me {x475}.
            My family experienced a tragic time when {x476} happened. I have always been a {x477} person and although I was
            {x478}, I made sure that I would still be able to {x479}.
            YOU HAD TO MAKE IN YOUR LIFE???HAD TO MAKE IN YOUR LIFE???Would you make the same choice again?????
            The most difficult choice that I made was {x480}. I do not regret / regret it until now and if
            I would be given a chance to choose a different option, I would {x481}. Throughout the years, I really didn???t travel much / went to a lot of places but the most memorable experience I had
            while traveling was when I went to {x482} alone / with {x483}. There, I / we did
            activities such as {x484}. The first time I rode an airplane was when I was off to {x485} when I was {x486} years old. I had to go there because of
            {x487}. (No) I did not get the chance to travel abroad but I bet I would love to see {x488}.
            (Yes) I had the opportunity of traveling abroad and it was {x489}! I enjoyed {x490} because {x491}.
            Among all the tourist spots and vacation places that I have been to, I can say that the most interesting and exciting
            was when I went
            to {x492}. It was special because {x493}.
            I {x494} helping people because I believe that {x495}. One person that
            I extended my helping hands to was named {x496}.
            He/she needed assistance in {x497} so I {x498}.
            I also dedicated myself to a cause / organization for the {x499}. I participated in it with an
            open heart because {x500}.
            How did you benefit from it???
            I was also given the chance to join competitive activities like {x501} which helped me grow in
            a way that {x502}.
            Being on earth for {x503} years is a lot of work and over the years I did many {x504} things. Thankfully, my efforts were
            professionally recognized when I {x505}. Upon receiving my award, I felt {x506}.
            The most important invention in my lifetime was {x507}. I will be eternally grateful that it
            existed because
            {x508}.
            Some of the most remarkable political / international events that I witnessed or participated in while I am living were
            {x509}.
            These were memorable because {x510}.
            Science has always {x511} me but, in particular, {x512} piqued my
            interest.
            Growing up to be who I am today and comparing my upbringing to the youth of the current times, I can say that we are
            very
            similar / different in ways such as {x513}. This might be due to the fact that {x514} nowadays
            compared to back then.
            Even though I was {x515}, I don???t think I would want to change that about how I lived my life
            even if I would be given a chance to do
            so.
            Although, I guess I would have changed {x516} because {x517}.
            In the next ten years, I wish my family will become {x518} so that {x519}.
            For the world to be a better and happier place however, I hope that {x520} will change and
            {x521}
            can be more {x522}.
            Inspiration????How great it is??to have the freedom to dream??and the opportunity??to make those dreams come true.??

            The people I would like to thank for helping me be the person I am today are {x523}. They
            helped me
            {x524}.
            Whenever I needed help, I would always approach {x525} and he/she always had the answers that
            could make me {x526}.
            (No) Religion did not really play a significant role in my life.
            (Yes) Religion helped me be a {x527} person. I relied on my faith every time I {x528}.
            A poem/passage/quote that I learned to live by or admired sincerely was {x529} by {x530}. This is due to the fact that
            {x531}.
            If worst comes to worst and I am only allowed to keep a single family photo, it would be that of {x532}. This is {x533}
            for me because it reminds me of {x534}.
            Perhaps, the greatest possession that I have is my {x535}. It is unbeatable by any other
            because {x536}.
            The greatest gifts in my life are {x537}. I will forever be grateful for these.
            (No) I never felt that I was born to become someone.
            (Yes) I have always felt that I was born to be {x538} -- that I was called to {x539}.
            Back when I was little, I looked up to {x540} the most because {x541}.
            Somehow, I grew up to be
            closely similar to/different from them.
            A celebrity that I admired was {x542} because of his/her {x543}.
            If not, who would you like to hear and why?????
            (No) I have never been able to listen to a public speaker but if I would be given the chance, I want to hear {x544} because he/she
            {x545}.
            (Yes) I was able to witness {x546} speaking live and it greatly impacted me in a way that
            {x547}.

            What are some of the insights that you???ve received?????
            One book that has always made a big impression on me was {x548} by {x549}. I loved this author???s works because
            they taught me that {x550}.
            When I was young, I was told by {x551} that I should {x552}. They
            taught me this lesson
            when I was {x553}.
            To be able to work well with other people, one should be {x554}. It requires {x555} to build a lasting relationship.
            Success is something that {x556}. It does not {x557} and it is not
            {x558}.
            The secret to it would be {x559}. That is what I realized in my life on earth.
            CHARACTERISTICS OF A GOOD FRIEND?????
            One can only be considered a good friend if they are {x560}, {x561},
            and {x562}. If not, then there must be
            {x563}.
            What I value most about my family is the fact that {x564}. Even though there are hardships,
            we {x565} together.


            My life on earth has been emotionally {x566}, physically {x567}, and
            wholly {x568}. People have come
            and gone, seasons have changed countless times, and days have been numbered one by one. The single most important lesson
            I???ve learned in this {x569} world is that {x570}.
            The greatest advice I can give right now is that {x571}. I am hoping that people will listen and that my family will deem this as unforgettable and {x572}.
            PLEASE RECORD ANY OTHER INFORMATION YOU WISH TO SHARE """

        obj = Stroy(owner=request.user,
                    story_name='First Story', the_story=male)
        obj.save()
    return render(request, 'story/temp.html'


def female_story(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        x5 = request.POST.get('x5')
        x6 = request.POST.get('x6')
        x7 = request.POST.get('x7')
        x8 = request.POST.get('x8')
        x9 = request.POST.get('x9')
        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')
        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')
        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')
        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')
        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')
        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')
        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')
        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')
        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')
        x100 = request.POST.get('x100')
        x101 = request.POST.get('x101')
        x102 = request.POST.get('x102')
        x103 = request.POST.get('x103')
        x104 = request.POST.get('x104')
        x105 = request.POST.get('x105')
        x106 = request.POST.get('x106')
        x107 = request.POST.get('x107')
        x108 = request.POST.get('x108')
        x109 = request.POST.get('x109')
        x110 = request.POST.get('x110')
        x111 = request.POST.get('x111')
        x112 = request.POST.get('x112')
        x113 = request.POST.get('x113')
        x114 = request.POST.get('x114')
        x115 = request.POST.get('x115')
        x116 = request.POST.get('x116')
        x117 = request.POST.get('x117')
        x118 = request.POST.get('x118')
        x119 = request.POST.get('x119')
        x120 = request.POST.get('x120')
        x121 = request.POST.get('x121')
        x122 = request.POST.get('x122')
        x123 = request.POST.get('x123')
        x124 = request.POST.get('x124')
        x125 = request.POST.get('x125')
        x126 = request.POST.get('x126')
        x127 = request.POST.get('x127')
        x128 = request.POST.get('x128')
        x129 = request.POST.get('x129')
        x130 = request.POST.get('x130')
        x131 = request.POST.get('x131')
        x132 = request.POST.get('x132')
        x133 = request.POST.get('x133')
        x134 = request.POST.get('x134')
        x135 = request.POST.get('x135')
        x136 = request.POST.get('x136')
        x137 = request.POST.get('x137')
        x138 = request.POST.get('x138')
        x139 = request.POST.get('x139')
        x140 = request.POST.get('x140')
        x141 = request.POST.get('x141')
        x142 = request.POST.get('x142')
        x143 = request.POST.get('x143')
        x144 = request.POST.get('x144')
        x145 = request.POST.get('x145')
        x146 = request.POST.get('x146')
        x147 = request.POST.get('x147')
        x148 = request.POST.get('x148')
        x149 = request.POST.get('x149')
        x150 = request.POST.get('x150')
        x151 = request.POST.get('x151')
        x152 = request.POST.get('x152')
        x153 = request.POST.get('x153')
        x154 = request.POST.get('x154')
        x155 = request.POST.get('x155')
        x156 = request.POST.get('x156')
        x157 = request.POST.get('x157')
        x158 = request.POST.get('x158')
        x159 = request.POST.get('x159')
        x160 = request.POST.get('x160')
        x161 = request.POST.get('x161')
        x162 = request.POST.get('x162')
        x163 = request.POST.get('x163')
        x164 = request.POST.get('x164')
        x165 = request.POST.get('x165')
        x166 = request.POST.get('x166')
        x167 = request.POST.get('x167')
        x168 = request.POST.get('x168')
        x169 = request.POST.get('x169')
        x170 = request.POST.get('x170')
        x171 = request.POST.get('x171')
        x172 = request.POST.get('x172')
        x173 = request.POST.get('x173')
        x174 = request.POST.get('x174')
        x175 = request.POST.get('x175')
        x176 = request.POST.get('x176')
        x177 = request.POST.get('x177')
        x178 = request.POST.get('x178')
        x179 = request.POST.get('x179')
        x180 = request.POST.get('x180')
        x181 = request.POST.get('x181')
        x182 = request.POST.get('x182')
        x183 = request.POST.get('x183')
        x184 = request.POST.get('x184')
        x185 = request.POST.get('x185')
        x186 = request.POST.get('x186')
        x187 = request.POST.get('x187')
        x188 = request.POST.get('x188')
        x189 = request.POST.get('x189')
        x190 = request.POST.get('x190')
        x191 = request.POST.get('x191')
        x192 = request.POST.get('x192')
        x193 = request.POST.get('x193')
        x194 = request.POST.get('x194')
        x195 = request.POST.get('x195')
        x196 = request.POST.get('x196')
        x197 = request.POST.get('x197')
        x198 = request.POST.get('x198')
        x199 = request.POST.get('x199')
        x200 = request.POST.get('x200')
        x201 = request.POST.get('x201')
        x202 = request.POST.get('x202')
        x203 = request.POST.get('x203')
        x204 = request.POST.get('x204')
        x205 = request.POST.get('x205')
        x206 = request.POST.get('x206')
        x207 = request.POST.get('x207')
        x208 = request.POST.get('x208')
        x209 = request.POST.get('x209')
        x210 = request.POST.get('x210')
        x211 = request.POST.get('x211')
        x212 = request.POST.get('x212')
        x213 = request.POST.get('x213')
        x214 = request.POST.get('x214')
        x215 = request.POST.get('x215')
        x216 = request.POST.get('x216')
        x217 = request.POST.get('x217')
        x218 = request.POST.get('x218')
        x219 = request.POST.get('x219')
        x220 = request.POST.get('x220')
        x221 = request.POST.get('x221')
        x222 = request.POST.get('x222')
        x223 = request.POST.get('x223')
        x224 = request.POST.get('x224')
        x225 = request.POST.get('x225')
        x226 = request.POST.get('x226')
        x227 = request.POST.get('x227')
        x228 = request.POST.get('x228')
        x229 = request.POST.get('x229')
        x230 = request.POST.get('x230')
        x231 = request.POST.get('x231')
        x232 = request.POST.get('x232')
        x233 = request.POST.get('x233')
        x234 = request.POST.get('x234')
        x235 = request.POST.get('x235')
        x236 = request.POST.get('x236')
        x237 = request.POST.get('x237')
        x238 = request.POST.get('x238')
        x239 = request.POST.get('x239')
        x240 = request.POST.get('x240')
        x241 = request.POST.get('x241')
        x242 = request.POST.get('x242')
        x243 = request.POST.get('x243')
        x244 = request.POST.get('x244')
        x245 = request.POST.get('x245')
        x246 = request.POST.get('x246')
        x247 = request.POST.get('x247')
        x248 = request.POST.get('x248')
        x249 = request.POST.get('x249')
        x250 = request.POST.get('x250')
        x251 = request.POST.get('x251')
        x252 = request.POST.get('x252')
        x253 = request.POST.get('x253')
        x254 = request.POST.get('x254')
        x255 = request.POST.get('x255')
        x256 = request.POST.get('x256')
        x257 = request.POST.get('x257')
        x258 = request.POST.get('x258')
        x259 = request.POST.get('x259')
        x260 = request.POST.get('x260')
        x261 = request.POST.get('x261')
        x262 = request.POST.get('x262')
        x263 = request.POST.get('x263')
        x264 = request.POST.get('x264')
        x265 = request.POST.get('x265')
        x266 = request.POST.get('x266')
        x267 = request.POST.get('x267')
        x268 = request.POST.get('x268')
        x269 = request.POST.get('x269')
        x270 = request.POST.get('x270')
        x271 = request.POST.get('x271')
        x272 = request.POST.get('x272')
        x273 = request.POST.get('x273')
        x274 = request.POST.get('x274')
        x275 = request.POST.get('x275')
        x276 = request.POST.get('x276')
        x277 = request.POST.get('x277')
        x278 = request.POST.get('x278')
        x279 = request.POST.get('x279')
        x280 = request.POST.get('x280')
        x281 = request.POST.get('x281')
        x282 = request.POST.get('x282')
        x283 = request.POST.get('x283')
        x284 = request.POST.get('x284')
        x285 = request.POST.get('x285')
        x286 = request.POST.get('x286')
        x287 = request.POST.get('x287')
        x288 = request.POST.get('x288')
        x289 = request.POST.get('x289')
        x290 = request.POST.get('x290')
        x291 = request.POST.get('x291')
        x292 = request.POST.get('x292')
        x293 = request.POST.get('x293')
        x294 = request.POST.get('x294')
        x295 = request.POST.get('x295')
        x296 = request.POST.get('x296')
        x297 = request.POST.get('x297')
        x298 = request.POST.get('x298')
        x299 = request.POST.get('x299')
        x300 = request.POST.get('x300')
        x301 = request.POST.get('x301')
        x302 = request.POST.get('x302')
        x303 = request.POST.get('x303')
        x304 = request.POST.get('x304')
        x305 = request.POST.get('x305')
        x306 = request.POST.get('x306')
        x307 = request.POST.get('x307')
        x308 = request.POST.get('x308')
        x309 = request.POST.get('x309')
        x310 = request.POST.get('x310')
        x311 = request.POST.get('x311')
        x312 = request.POST.get('x312')
        x313 = request.POST.get('x313')
        x314 = request.POST.get('x314')
        x315 = request.POST.get('x315')
        x316 = request.POST.get('x316')
        x317 = request.POST.get('x317')
        x318 = request.POST.get('x318')
        x319 = request.POST.get('x319')
        x320 = request.POST.get('x320')
        x321 = request.POST.get('x321')
        x322 = request.POST.get('x322')
        x323 = request.POST.get('x323')
        x324 = request.POST.get('x324')
        x325 = request.POST.get('x325')
        x326 = request.POST.get('x326')
        x327 = request.POST.get('x327')
        x328 = request.POST.get('x328')
        x329 = request.POST.get('x329')
        x330 = request.POST.get('x330')
        x331 = request.POST.get('x331')
        x332 = request.POST.get('x332')
        x333 = request.POST.get('x333')
        x334 = request.POST.get('x334')
        x335 = request.POST.get('x335')
        x336 = request.POST.get('x336')
        x337 = request.POST.get('x337')
        x338 = request.POST.get('x338')
        x339 = request.POST.get('x339')
        x340 = request.POST.get('x340')
        x341 = request.POST.get('x341')
        x342 = request.POST.get('x342')
        x343 = request.POST.get('x343')
        x344 = request.POST.get('x344')
        x345 = request.POST.get('x345')
        x346 = request.POST.get('x346')
        x347 = request.POST.get('x347')
        x348 = request.POST.get('x348')
        x349 = request.POST.get('x349')
        x350 = request.POST.get('x350')
        x351 = request.POST.get('x351')
        x352 = request.POST.get('x352')
        x353 = request.POST.get('x353')
        x354 = request.POST.get('x354')
        x355 = request.POST.get('x355')
        x356 = request.POST.get('x356')
        x357 = request.POST.get('x357')
        x358 = request.POST.get('x358')
        x359 = request.POST.get('x359')
        x360 = request.POST.get('x360')
        x361 = request.POST.get('x361')
        x362 = request.POST.get('x362')
        x363 = request.POST.get('x363')
        x364 = request.POST.get('x364')
        x365 = request.POST.get('x365')
        x366 = request.POST.get('x366')
        x367 = request.POST.get('x367')
        x368 = request.POST.get('x368')
        x369 = request.POST.get('x369')
        x370 = request.POST.get('x370')
        x371 = request.POST.get('x371')
        x372 = request.POST.get('x372')
        x373 = request.POST.get('x373')
        x374 = request.POST.get('x374')
        x375 = request.POST.get('x375')
        x376 = request.POST.get('x376')
        x377 = request.POST.get('x377')
        x378 = request.POST.get('x378')
        x379 = request.POST.get('x379')
        x380 = request.POST.get('x380')
        x381 = request.POST.get('x381')
        x382 = request.POST.get('x382')
        x383 = request.POST.get('x383')
        x384 = request.POST.get('x384')
        x385 = request.POST.get('x385')
        x386 = request.POST.get('x386')
        x387 = request.POST.get('x387')
        x388 = request.POST.get('x388')
        x389 = request.POST.get('x389')
        x390 = request.POST.get('x390')
        x391 = request.POST.get('x391')
        x392 = request.POST.get('x392')
        x393 = request.POST.get('x393')
        x394 = request.POST.get('x394')
        x395 = request.POST.get('x395')
        x396 = request.POST.get('x396')
        x397 = request.POST.get('x397')
        x398 = request.POST.get('x398')
        x399 = request.POST.get('x399')
        x400 = request.POST.get('x400')
        x401 = request.POST.get('x401')
        x402 = request.POST.get('x402')
        x403 = request.POST.get('x403')
        x404 = request.POST.get('x404')
        x405 = request.POST.get('x405')
        x406 = request.POST.get('x406')
        x407 = request.POST.get('x407')
        x408 = request.POST.get('x408')
        x409 = request.POST.get('x409')
        x410 = request.POST.get('x410')
        x411 = request.POST.get('x411')
        x412 = request.POST.get('x412')
        x413 = request.POST.get('x413')
        x414 = request.POST.get('x414')
        x415 = request.POST.get('x415')
        x416 = request.POST.get('x416')
        x417 = request.POST.get('x417')
        x418 = request.POST.get('x418')
        x419 = request.POST.get('x419')
        x420 = request.POST.get('x420')
        x421 = request.POST.get('x421')
        x422 = request.POST.get('x422')
        x423 = request.POST.get('x423')
        x424 = request.POST.get('x424')
        x425 = request.POST.get('x425')
        x426 = request.POST.get('x426')
        x427 = request.POST.get('x427')
        x428 = request.POST.get('x428')
        x429 = request.POST.get('x429')
        x430 = request.POST.get('x430')
        x431 = request.POST.get('x431')
        x432 = request.POST.get('x432')
        x433 = request.POST.get('x433')
        x434 = request.POST.get('x434')
        x435 = request.POST.get('x435')
        x436 = request.POST.get('x436')
        x437 = request.POST.get('x437')
        x438 = request.POST.get('x438')
        x439 = request.POST.get('x439')
        x440 = request.POST.get('x440')
        x441 = request.POST.get('x441')
        x442 = request.POST.get('x442')
        x443 = request.POST.get('x443')
        x444 = request.POST.get('x444')
        x445 = request.POST.get('x445')
        x446 = request.POST.get('x446')
        x447 = request.POST.get('x447')
        x448 = request.POST.get('x448')
        x449 = request.POST.get('x449')
        x450 = request.POST.get('x450')
        x451 = request.POST.get('x451')
        x452 = request.POST.get('x452')
        x453 = request.POST.get('x453')
        x454 = request.POST.get('x454')
        x455 = request.POST.get('x455')
        x456 = request.POST.get('x456')
        x457 = request.POST.get('x457')
        x458 = request.POST.get('x458')
        x459 = request.POST.get('x459')
        x460 = request.POST.get('x460')
        x461 = request.POST.get('x461')
        x462 = request.POST.get('x462')
        x463 = request.POST.get('x463')
        x464 = request.POST.get('x464')
        x465 = request.POST.get('x465')
        x466 = request.POST.get('x466')
        x467 = request.POST.get('x467')
        x468 = request.POST.get('x468')
        x469 = request.POST.get('x469')
        x470 = request.POST.get('x470')
        x471 = request.POST.get('x471')
        x472 = request.POST.get('x472')
        x473 = request.POST.get('x473')
        x474 = request.POST.get('x474')
        x475 = request.POST.get('x475')
        x476 = request.POST.get('x476')
        x477 = request.POST.get('x477')
        x478 = request.POST.get('x478')
        x479 = request.POST.get('x479')
        x480 = request.POST.get('x480')
        x481 = request.POST.get('x481')
        x482 = request.POST.get('x482')
        x483 = request.POST.get('x483')
        x484 = request.POST.get('x484')
        x485 = request.POST.get('x485')
        x486 = request.POST.get('x486')
        x487 = request.POST.get('x487')
        x488 = request.POST.get('x488')
        x489 = request.POST.get('x489')
        x490 = request.POST.get('x490')
        x491 = request.POST.get('x491')
        x492 = request.POST.get('x492')
        x493 = request.POST.get('x493')
        x494 = request.POST.get('x494')
        x495 = request.POST.get('x495')
        x496 = request.POST.get('x496')
        x497 = request.POST.get('x497')
        x498 = request.POST.get('x498')
        x499 = request.POST.get('x499')
        x500 = request.POST.get('x500')
        x501 = request.POST.get('x501')
        x502 = request.POST.get('x502')
        x503 = request.POST.get('x503')
        x504 = request.POST.get('x504')
        x505 = request.POST.get('x505')
        x506 = request.POST.get('x506')
        x507 = request.POST.get('x507')
        x508 = request.POST.get('x508')
        x509 = request.POST.get('x509')
        x510 = request.POST.get('x510')
        x511 = request.POST.get('x511')
        x512 = request.POST.get('x512')
        x513 = request.POST.get('x513')
        x514 = request.POST.get('x514')
        x515 = request.POST.get('x515')
        x516 = request.POST.get('x516')
        x517 = request.POST.get('x517')
        x518 = request.POST.get('x518')
        x519 = request.POST.get('x519')
        x520 = request.POST.get('x520')
        x521 = request.POST.get('x521')
        x522 = request.POST.get('x522')
        x523 = request.POST.get('x523')
        x524 = request.POST.get('x524')
        x525 = request.POST.get('x525')
        x526 = request.POST.get('x526')
        x527 = request.POST.get('x527')
        x528 = request.POST.get('x528')
        x529 = request.POST.get('x529')
        x530 = request.POST.get('x530')
        x531 = request.POST.get('x531')
        x532 = request.POST.get('x532')
        x533 = request.POST.get('x533')
        x534 = request.POST.get('x534')
        x535 = request.POST.get('x535')
        x536 = request.POST.get('x536')
        x537 = request.POST.get('x537')
        x538 = request.POST.get('x538')
        x539 = request.POST.get('x539')
        x540 = request.POST.get('x540')
        x541 = request.POST.get('x541')
        x542 = request.POST.get('x542')
        x543 = request.POST.get('x543')
        x544 = request.POST.get('x544')
        x545 = request.POST.get('x545')
        x546 = request.POST.get('x546')
        x547 = request.POST.get('x547')
        x548 = request.POST.get('x548')
        x549 = request.POST.get('x549')
        x550 = request.POST.get('x550')
        x551 = request.POST.get('x551')
        x552 = request.POST.get('x552')
        x553 = request.POST.get('x553')
        x554 = request.POST.get('x554')
        x555 = request.POST.get('x555')
        x556 = request.POST.get('x556')
        x557 = request.POST.get('x557')
        x558 = request.POST.get('x558')
        x559 = request.POST.get('x559')
        x560 = request.POST.get('x560')
        x561 = request.POST.get('x561')
        x562 = request.POST.get('x562')
        x563 = request.POST.get('x563')
        x564 = request.POST.get('x564')
        x565 = request.POST.get('x565')
        x566 = request.POST.get('x566')
        x567 = request.POST.get('x567')
        x568 = request.POST.get('x568')
        x569 = request.POST.get('x569')
        x570 = request.POST.get('x570')
        x571 = request.POST.get('x571')
        x572 = request.POST.get('x572')
        x580 = request.POST.get('x580')
        x581 = request.POST.get('x581')
        male = f"""I was born on the {x1} in {x2}, a city in {x3} at {x4} hospital.
            My full name is {x5} .

            The people who decided on this name are {x6}.
            I was named this way because {x7}.Sometimes, I go by the nickname {x8} which I got from {x9}.
            I have a beautiful mother named {x10}. She was born on {x11} in {x12}.
            The place she grew up in {x13} was lovely just like her.
            Meanwhile, my father, {x14}, was born on the {x15}. He was raised in
            the city of {x16}.


            To complete my family, I have {x17} siblings.
            Their names are {x18}. They were born in {x19}. My mother gave birth
            to {20} on {x21}. On the other hand,
            {x22} was born on {x23}.
            I have a beautiful/handsome sister/brother who goes by the name {x24}. She/he was born on the
            {x25} in
            {x26}.
            My mother was raised well by her parents, {x7} and {x27}. My
            grandmother was named {x28}. Her birthday was on
            the {x29}; whereas, my grandpa, {x30}, was born on {x31} in the village of {x32}.


            On my father???s side, I was blessed with the lives of my grandma, {x33}, and my grandpa, {x34}.
            Granny was born on {x35} in {x36}. My grandfather???s birth date,
            however, was on {x37}. His family
            gleefully welcomed him on this day in the city of {x38}.



            I have the most gorgeous wife. She was named {x39} but I call her {x40}. I am thankful that she was successfully given
            birth to on the{x41} in the wonderful city of {x42}.

            {x43} and I were blessed with {x44} children who we named as {x45}.
            {x46} was born on {x47} in {x48}. On the
            other hand, {x49}???s birthdate is on {x50}. My wife gave
            birth to him/her in {x51}.



            Over the years, my children grew up and had their own kids, too. My adorable grandkids are named {x580} and {x581}.
            The first one is born in {x52} on the {x53}.
            {x54} was born on {x55} in the city of {x55}.



            I spend most of my free time {x56} while drinking {x57}.


            My most favorite sport is {x58} because I think it is {x59}


            My go-to vacation spot is {x61}. I find it {x62}.


            The meal that I enjoy the most is {x63}.


            My favorite song is called {x64}; it is sung by {x65}. The reason why
            I love it is that it reminds me of
            {x67}.


            Currently, my favorite television show is {x68}. Back then, I really loved the series {x69}.



            I have watched the movie {x70} several times already and I never get tired of it because it is
            {x71}.


            My hobbies are {x72}, {x73}, and {x74}. On
            the weekends, I also {x75} with my {x76}.



            The social gatherings that I usually enjoy are {x77}.


            My greatest talent is {x78}. I have used it in many ways throughout my life such as when I
            {x79}.


            The best characteristic that I love about myself is my {x80}.

            Sometimes, I wish I could stop being {x81}.



            Currently, I am living a {x81} life here in {x82} with my {x83}.
            On the weekdays, I spend most of my time {x84}. By the end of the day, I would feel {x85} and {x86}.



            I grew up in a {x87} neighborhood where I met various interesting people like {x88}.
            Remembering it, I can say that it was actually a {x89} place.


            My childhood home was {x90}. I enjoyed all of the {x91} mornings and
            {x92} nights in it. The house was
            suitable for a family of {x93} people. My time there was {x94}.



            My favorite place in this {x95} house was the {x96}. It had a special
            place in my heart because it {x97}.




            When I was younger, I had to do chores like {x98}.


            ({x99}) I got a daily/weekly/monthly allowance worth {x100}.



            The indoor activity that I enjoyed the most was {x101}. This was because {x102}.


            Back then, I really enjoyed {x103} outside the house.


            As a child, I was particularly skilled at {x104}.



            I also had some toys that cheered me up on sad days. These are {x105}.



            I had a special place that I called ???mine.??? It was this {x106} space filled with {x107}. I used to {x108} a lot when
            I stayed here.


            As a child, I always anticipated going out to {x109}.



            Being a boy, I {x110} not enjoy reading.
            (If yes) I liked collecting {x111} books!


            of this experience???{x112}
            I lived in a {x113} (Religious/Non-Religious) family.
            (If religious). I attended a church called {x114} which was located in {x115}. I remember the times when I {x116}.

            I {x117} baptized or dedicated as an infant.
            (If baptized) As an infant, I was baptized by {x118} in {x119}. My
            {x120} attended the celebration



            Some of the childhood experiences that helped me become who I am right now are {x121}.



            I remember having a childhood friend named {x122}. He/she was very {x123} and we had a {x124} time together.



            From my childhood, I will be eternally grateful for the {x125}. Because of it, I grew up to be
            a {x126} person.
            Family LIFE
            50 A family is a circle of love?????formed by memories,??filled with devotion.????



            My favorite memory with my dad was when {x127}. This is a special event for me because {x128}.



            My father???s insights on life and its adventures was {x129}. This made me become more {x130} regarding my own life.


            My father and I used to {x131} together and I really enjoyed it because {x132}.


            I think I have grown up to be like my father when it comes to my {x133}. I always think that I
            got this from him.


            One thing my dad always said was {x134}. I believe that this is actually a great {x135} and it helped me
            establish myself.


            My father worked as a/an {x136}. This job piqued / did not pique my interest because {x137}.


            One of the most memorable things about my mother from when I was a little boy was how she {x138}. This is because {x139}.

            My mom always had a {x140} outlook towards life. This attitude of hers affected me in a way
            that I became more {x141}.



            I am similar to her because she is {x142} just like me. My mother is the most {x143} woman I have ever met and I love her
            for it.


            Back when I was a child, I really liked {x144} with my mom. Until now, I still feel {x145} whenever I remember this.




            My mother???s occupation was {x146}. This helped me decide on my future career because I found it
            {x147} how she
            {x148}.


            My family was {x149}. We encountered problems such as {x150} and it
            was hard for me growing up. But
            I am now {x151} about my life. These circumstances have made me {x152}
            and {x153}.

            As I was growing up, my parents requested that I {x154}.


            This formed my mindset regarding parenting. In complete honesty, I actually require my children to {x155}, similar to /
            different from the obligations I had as a kid.


            Some of the qualities that my parents nurtured in me are my characteristics of being {x156} and
            {x157}. I am thankful for these.



            My parents always told me to be a {x158} person. Of course, I valued their encouragement
            because I loved them.



            I also loved my siblings/sister/brother so much. My fondest memories of them/him/her was that time when {x159}.

            Of course, being young means you get to enjoy the beauty of life without heavily thinking of the consequences. I played
            around with my
            siblings/brother/sister and we used to {x160}. It was funny for me back then but looking back,
            I think {x161}.
            My siblings/brother/sister and I were {x162}. We had {x163} days
            together.
            In addition to our lovely family, we had a pet {x164} / pets named {x165}. He/she/they were adorable!
            The thing I loved most about having {x166} growing up with me was {x167}. I loved {x168} with {x169}!
            On regular days, my family {x170} together. In the summer, we would often go {x171}. But most especially,
            we loved spending time together, either by {x172} or {x173}.
            My early memories of my grandparents was how they {x174}. My grandma would always {x175} while my grandpa {x176}.

            They lived in a lovely place in {x177}. Around their area, there were many {x178}. It was a {x179} neighborhood.
            My grandmother worked as a {x180} and my grandpa did some {x181} job.

            Whenever my family visited them / whenever they visited us, I remember that we always had an amazing time together. My
            grandma and
            grandpa prepares a delicious meal for us. Their {x182} was my favorite!

            I loved being with my grandparents because they were {x183}. I always watched them {x184} . They cared for me and my
            siblings/brother/sister.
            A valuable lesson that I learned from being with them was that {x185}. Aside from this, I was
            also inspired by them to be a {x186}
            person.
            The only things I remember about my great-grandparents are that they {x187}.
            I believe that my ancestors were {x188} and that I might have a/an {x189} origin.
            My favorite home-cooked meal was {x190} because it was honestly delicious and {x191}! It reminds me of {x192}.
            Whenever my family and I {x193} together, we would always prepare {x194}.
            We used to go out for dinner frequently/sometimes. When we do, I would always request that we go to {x195} or try other restaurants
            that serve {x196}.
            (Yes) Our house was a great place for celebrations. I remember having company often. My family???s friends or some of our
            other relatives
            would always come to visit or {x197} with us.
            (No) Although we were a happy family, we did not often have company perhaps because our place was {x198}.
            My family outings were {x199}! We would always go to {x200} and {x201} together. Holidays are my {x202} favorite season!
            In the winter, I remember {x203} with my siblings/brother/sister. As a whole family, we liked
            playing {x204}. My favorite
            winter food was {x205}. And drinks? Of course, {x206}.
            Family reunions are {x207} for me. I enjoyed {x208} whenever we held
            one.
            (No) I was not really close to my relatives.
            (Yes) I had close relationships with my other relatives especially with my {x209}. I am happy
            about these because I could always
            {x210} to them whenever I am {x211}.

            Every time I think about my family, the first thing that comes to mind was {x212}. I feel like
            I associated them with it because of
            the {x213} they bring to my life.

            Knowledge is the power??that gives us wings to soar.??

            I attended elementary at {x214} in {x215}. I often rode the {x216} to school and back OR I often biked/walked to
            school alone/with my {x217}.My earliest memories of going to {x218} was that I would always {x219}
            in {x220} Class. I also remember hanging out
            with my childhood friends named {x221} and {x222}.
            92 WHAT DID YOU ENJOY?? MOST ABOUT ELEMENTARY SCHOOL?????
            One thing I loved most about elementary was {x223} on {x224} days.
            But, I really hated that I had to {x225}.
            Next, I attended middle school at {x226}. Every day, I would go there via {x227}. Sometimes, I would {x228}.
            When I was in high school, I attended {x229}. It was a very {x230}
            school and I met a lot of {x231} people there.
            My favorite subjects in middle school were {x232} and {x233} because
            {x234}.
            Meanwhile, in high school, I really liked going to {x235} class. The teacher was really {x236} and my classmates were
            {x237}.
            Some extracurricular activities that I enjoyed the most were {x238}. I chose these because
            {x239}.
            Over the years, I have received some special awards such as {x240}.
            I had a favorite teacher whose name was {x241}. I can say that she/he had a big influence on
            shaping who I am now by {x242}.
            Back when I was still in school, there were many fashion trends that arose such as {x243}.
            (Yes) I participated in them because {x244}.
            (No) I did not participate much when it comes to these because {x245}.
            The most popular songs that I remember around the time I was studying were {x246}. I really
            {x247} this kind of music.
            Meanwhile, the highest grossing movies were {x248}. People {x249}
            these so much!
            The television shows that were much awaited were {x250}.
            Lastly, celebrities such as {x251} were having their primes then.
            The parties that I attended were mostly {x252}. Some of the party-goers were from {x253}. I can still remember
            how {x254} the crowd was.
            (No) I didn???t have a car when I was in high school but if I did it probably would be a __________.
            (Yes) I had a car when I was a teenager and it was a {x255}. I was {x256} about how it looks like.
            I really went places with that car.
            My middle school and high school years were a bit difficult because of {x257}. But, as a whole
            I think I really {x258}
            my teenage years.
            DURING YOUR MIDDLE SCHOOL AND HIGH SCHOOL YEARS???
            I am happy that I got to {x259} while I was schooling. It was a great privilege for me.
            change with time?????
            During this time, I was thinking about my goal of becoming a {x260} and I really hoped to
            achieve my dreams such as
            that of {x261}. Over time, I continued/stopped inching towards these goals.
            After graduation, I chose to follow the path of becoming a {x262}.
            I went to college / a career training school called {x263} in the city of {x264}. I took up a degree in the field of
            {x265}.
            I had to move away from home to continue studying and it was {x266}. I was looking forward to
            {x267} but I really felt
            {x268} when I was away from my family.
            I lived in an apartment/dorm nearby. It was {x269}, {x270}, and {x271}. I had a {x272} time studying when I was
            there.
            (with roommate) I had a roommate whose name was {x273}. He/she was a {x274} person.
            My most favorite college memories were the one at {x275} with my {x276}. Those experiences were {x277}
            and unforgettable.
            On??the Job??

            Any job can be made great.??It???s the worker???not the work?????that counts

            When I was young, I tried to gain money by {x278}. My earnings were used to pay for my {x279}.


            My first career-oriented job after graduation was a {x280} at {x281}.
            Here, I would be the one responsible for
            {x282}.
            When I found out that I got accepted in this job, I was very {x283}. I thought that this can
            help me in {x284}.
            The one thing I love most about my first job was {x285}. The environment in the workplace was
            also {x286}.
            Among the jobs that I tried and had in the past, the one in which I probably had the most fun was when I was working at
            {x287}
            as a {x288}. This is due to the fact that {x289}.

            Meanwhile, the worst job was in {x290}. I mostly did not enjoy working here because of {x291}.
            The most rewarding out of all, however, was the job at {x292}. This is because I was {x293}. I really love
            {x294} about this job.
            Of course, some opportunities can only be achieved when you move out of your comfort zone. As for me, I had to move away
            when I
            was working at {x295} in {x296}. I felt {x297} because of it but I am {x298} that I took it.
            For some jobs, I had to go places for {x299} events. The most memorable place I visited while
            doing so was a {x300} in {x301}.
            I had a coworker / superior who displayed the role of a friendly and trustworthy mentor to me. His/her name was {x302} and
            he/she taught me how to {x303}.
            (If yes) Over the years, I was able to be a mentor to others, too. I believe it was a {x304}
            experience for me.
            (If no) I might not have been an official mentor to others myself, but I believe that I was also able to help my
            colleagues in various ways.

            At work, I met all types of people but I found {x305} friends, too.
            When I???m just at home, I like to work on {x306}.
            But, I usually avoid doing {x307} because {x308}.
            Love??AND??Marriage????
            130 When love touches our hearts,??happiness fills our days.??

            I remember having a crush on {x309} when I was younger. I believe she was the first person I
            truly admired.
            The first boy party that I attended was when I was {x310} years old. It was held at {x311}..
            My first kiss was {x312}. I remember how I felt really {x313}
            afterwards.
            My first ever date was {x314}. It went {x315}. I had a {x316} time with {x317}.
            When that happened, lovers usually {x318} when they went out together and hung out. The kind of
            date nights was very {x319}
            compared to now.
            I met my lovely wife when I was {x320} years old.


            I will be eternally grateful that our paths crossed on {x321} in {x322}. If it weren???t for the {x323},
            I wouldn???t have seen her.
            She was {x324}, {x325}, and {x326}. Those
            qualities really captured my attention.
            Initially, I thought that she was {x327}. Over time, I realized how {x328} my first impression was compared to how
            she really is.
            I courted her for {x329} months. She was definitely worth the wait.
            When we just started dating, we really loved {x330} together. Some other things that we enjoyed
            doing were {x331}
            and {x332}.
            I knew she was the one when {x333} after I realized that she could be {x334}.
            The marriage proposal was {x335} and I am sincerely {x336} about it!
            There were {x337} everywhere while I
            was waiting for her response.
            We officially tied the knot on {x338} at a {x339} in {x340}.


            I wore a {x341}.

            While she wore a beautiful and {x342} wedding dress/gown.??

            It was a small/big wedding. We had about {x343} guests.

            For our first dance as husband and wife, we swayed to the song entitled {x344} which was chosen
            because {x345}.
            The most remarkable memory of mine from that special day was {x346}.

            Recall a special moment or event from the honeymoon.??
            Our honeymoon was {x347}! We went to {x348} wherein we {x349}. What I loved most about this
            experience was the fact that {x350}.


            After getting married, we lived in {x351}. I clearly remember how {x352} our home was.


            Early into our marriage, we had {x353} nights where we would enjoy dinner together over a
            {x354}.
            We started thinking about having children when {x355}. I really looked forward to {x356} and seeing my wife
            {x357} for our kids.


            WHEN YOU WERE FIRST MARRIED???What were some of the fun things you did with them???
            As a couple, we had some close friends. The ones that we mostly hung out with were named {x358}.
            We would always {x359} together and it felt {x360}! I {x361} spending time with them.


            {x362} and I really loved {x363} whenever we had free time. Aside from
            this, we also enjoyed {x364}.
            For me, marriage has been rewarding because {x365}.
            To be able to withstand any hardship, I believe that the most important key to a healthy marriage is {x366}.
            Of course in our marriage we also had hard times wherein we needed to be there for each other more. These instances that
            required
            sharing and companionship happened when {x367}.
            My daily relationship with my loving wife has been {x368}. Right now, my favorite thing about
            being married to is {x369}.
            Parenting????
            To be a father is to protect,??nurture, and guide,??but most of all, to love.????


            When I found out that I was going to be a dad, I felt {x370}. I remember that day being a
            {x371}
            one.
            I lived in {x372}
            My FIRST CHILD WAS BORN on ??{x373}
            My growing family then lived at a {x374} in {x375}.


            Back then, our situation was {x376}.
            We had problems such as {x377} OR We did not have any problems.


            Every time I looked at my firstborn when he/she was an infant, I felt {x378}. Every day with
            him/her was really
            {x379}.


            Becoming a father was {x380}. It caused me to have a more {x381}
            outlook on life. I realized that {x382}.
            168 WHAT IS YOUR MOST VIVID MEMORY??OF YOUR CHILDREN???S EARLY YEARS?????
            I have some crystal clear memories of my children when they were still young. These include the time when {x383} and
            also that instance when {x384}.


            Back then, I really enjoyed {x386} with them. When they grew up a bit, we would always {x385}.
            Of course, there had to be some days that I would need to spend alone with my wife. Whenever we took the days off for
            our special dates,
            we would {x387}.

            As a parent, I believe that it is undeniable that I have similarities with my kids. These include {x388}.
            As for them, my kids are similar in a way that they are all {x389}. This might be because
            {x390}.
            My spouse and I tried to instill the qualities of being {x391}, {x392}, and {x393} to our kids.
            I know that I have been blessed to be a father because I get to experience {x394}. This is what
            I consider my greatest joy
            in this {x395} role.
            Because life is not perfect, our family had problems, too. The greatest challenge that I experienced as a dad to {x396} beautiful kids
            was {x397}.
            I was raised in a {x398} family which is similar/different to my children???s upbringing. They
            grew up in a {x399} house, a
            {x400} neighborhood, with {x401} parents.
            THAT YOU WISH YOU???D KNOWN WHEN YOU??FIRST BECAME A FATHER?????
            Sometimes, I wish that I knew better when I became a father to my firstborn. One thing that I learned through time that
            I could
            have known back when I was raising {x402} was {x403}.
            I am a {x404} person. Somehow I wish my kids can grow up to be {x405}
            -- opposite/similar to me.
            Being a father taught me a lot of {x406} lessons but to me the most important thing among all
            these is {x407}.
            This is due to the fact that {x408}.


            Life offers so many??wonderful things to share,??so many special joys to celebrate.????

            We would always {x409} on my birthday when I was young. The guests were usually {x410}. It was a {x411}
            celebration.


            My favorite memory of a birthday party was when {x412}. This happened on my {x413} th birthday.
            The most special presents that I ever received are {x414}. For me, they were wonderful because
            {x415}.
            I often requested that my parents cook/make/buy {x416} to serve on my birthdays. I really loved
            these food because
            {x417}.
            Apart from the celebration of my birth, I had other unique parties held at our humble abode. These include {x418}.
            The ambiance of the surroundings during this feast was {x419}. Guests had to wear {x420}.
            As a child, my favorite religious festivity is {x421}. We would {x422}
            together as a family and {x423}.
            We prepare meals such as {x424} to feast on.
            Among these types of celebrations, the main thing that stands out in my memory is {x425} due to
            the fact that
            {x426}.

            I really liked the {x427} that we buy/make during my childhood. It tasted {x428} and {x429}.
            My favorite christmas carol was {x420}. Right now, {x431} is my
            favorite.
            where??it??came??from?????
            What my family told us about Santa Claus was that he was/wasn???t real. I always knew/didn???t know where the gifts from my
            Christmas
            stocking / ornament came from.
            During these holidays, we often gave presents to each other. My most loved gift was the {x432}
            from my {x433}
            because {x434}.
            Meanwhile, the most memorable present that I gave someone was a {x435}. This was for my {x436}.
            I still remember how he/she {x437} it.
            Growing up, I always loved the religious tradition we had in our family. Now that I have my own, I continued to {x438}.
            As a parent, the most meaningful Christmas for me was when {x439} because {x440}.
            195 HOW DID YOU CELEBRATE THANKSGIVING???Did you have a favourite Thanksgiving tradition?????
            For Thanksgiving, my family usually {x441}. The tradition that I love most is {x442}.
            Preparing and eating Thanksgiving food is also {x443}.
            When I was a kid, I really {x444} Australia day. The neighborhood would always be {x445} and there were {x446}
            everywhere!
            What was your favourite Halloween treat?????
            I did/didn???t really enjoy halloween. I remember an especially fun costume worn by {x447}. It
            was a {x448}.
            I also {x449} to trick-or-treat! My favorite treat was {x450} since
            {x451}. One memory that I have of a really enjoyable holiday celebration was when {x452}. It happened around the time that {x453}. I think it was a meaningful experience for me because {x454}.
            Moment by moment,??day by day,??families create a lifetime of memories.??The happiest time of my life, I must say, is when {x455}. I cannot explain the joy that I felt because {x456}. To me, it???s an experience that cannot be beaten by anything else. Meanwhile, the saddest for me was when {x457}. I believe I had a {x458} time moving on from this
            because {x459}. Over the years, I had many commitments and responsibilities but there was a time wherein I was always occupied.
            The busiest I have ever been was when {x460}. It was due to the fact that {x461}. On the other hand, I had relaxing days, too, but I am confident to say that I was most comfortable and at ease when
            {x462}. A life-changing event that really influenced me in many ways was when {x463}. Somehow, it
            helped me {x464}. One political event that I participated in or witnessed over the years was {x465}. It made a
            really strong impression on for the reason that {x466}.  (I have) I served in the military back then. It was a {x467} experience, while at the same
            time, there were instances that {x468} me such as {x469}. (Other family members have) Some of my relatives had to serve in the military. I was really {x470} about it and it
            often {x471} me thinking about what was happening to them while in there.
            I can proudly say that I was able to {x472}. This had been fulfilling for me because {x473}.
            I have been in an accident/major surgery/long illness. This involved me being {x474}.
            It sincerely didn???t have / had a lasting effect on me because it made me {x475}.
            My family experienced a tragic time when {x476} happened. I have always been a {x477} person and although I was
            {x478}, I made sure that I would still be able to {x479}.
            YOU HAD TO MAKE IN YOUR LIFE???HAD TO MAKE IN YOUR LIFE???Would you make the same choice again?????
            The most difficult choice that I made was {x480}. I do not regret / regret it until now and if
            I would be given a chance to choose a different option, I would {x481}. Throughout the years, I really didn???t travel much / went to a lot of places but the most memorable experience I had
            while traveling was when I went to {x482} alone / with {x483}. There, I / we did
            activities such as {x484}. The first time I rode an airplane was when I was off to {x485} when I was {x486} years old. I had to go there because of
            {x487}. (No) I did not get the chance to travel abroad but I bet I would love to see {x488}.
            (Yes) I had the opportunity of traveling abroad and it was {x489}! I enjoyed {x490} because {x491}.
            Among all the tourist spots and vacation places that I have been to, I can say that the most interesting and exciting
            was when I went
            to {x492}. It was special because {x493}.
            I {x494} helping people because I believe that {x495}. One person that
            I extended my helping hands to was named {x496}.
            He/she needed assistance in {x497} so I {x498}.
            I also dedicated myself to a cause / organization for the {x499}. I participated in it with an
            open heart because {x500}.
            How did you benefit from it???
            I was also given the chance to join competitive activities like {x501} which helped me grow in
            a way that {x502}.
            Being on earth for {x503} years is a lot of work and over the years I did many {x504} things. Thankfully, my efforts were
            professionally recognized when I {x505}. Upon receiving my award, I felt {x506}.
            The most important invention in my lifetime was {x507}. I will be eternally grateful that it
            existed because
            {x508}.
            Some of the most remarkable political / international events that I witnessed or participated in while I am living were
            {x509}.
            These were memorable because {x510}.
            Science has always {x511} me but, in particular, {x512} piqued my
            interest.
            Growing up to be who I am today and comparing my upbringing to the youth of the current times, I can say that we are
            very
            similar / different in ways such as {x513}. This might be due to the fact that {x514} nowadays
            compared to back then.
            Even though I was {x515}, I don???t think I would want to change that about how I lived my life
            even if I would be given a chance to do
            so.
            Although, I guess I would have changed {x516} because {x517}.
            In the next ten years, I wish my family will become {x518} so that {x519}.
            For the world to be a better and happier place however, I hope that {x520} will change and
            {x521}
            can be more {x522}.
            Inspiration????How great it is??to have the freedom to dream??and the opportunity??to make those dreams come true.??

            The people I would like to thank for helping me be the person I am today are {x523}. They
            helped me
            {x524}.
            Whenever I needed help, I would always approach {x525} and he/she always had the answers that
            could make me {x526}.
            (No) Religion did not really play a significant role in my life.
            (Yes) Religion helped me be a {x527} person. I relied on my faith every time I {x528}.
            A poem/passage/quote that I learned to live by or admired sincerely was {x529} by {x530}. This is due to the fact that
            {x531}.
            If worst comes to worst and I am only allowed to keep a single family photo, it would be that of {x532}. This is {x533}
            for me because it reminds me of {x534}.
            Perhaps, the greatest possession that I have is my {x535}. It is unbeatable by any other
            because {x536}.
            The greatest gifts in my life are {x537}. I will forever be grateful for these.
            (No) I never felt that I was born to become someone.
            (Yes) I have always felt that I was born to be {x538} -- that I was called to {x539}.
            Back when I was little, I looked up to {x540} the most because {x541}.
            Somehow, I grew up to be
            closely similar to/different from them.
            A celebrity that I admired was {x542} because of his/her {x543}.
            If not, who would you like to hear and why?????
            (No) I have never been able to listen to a public speaker but if I would be given the chance, I want to hear {x544} because he/she
            {x545}.
            (Yes) I was able to witness {x546} speaking live and it greatly impacted me in a way that
            {x547}.

            What are some of the insights that you???ve received?????
            One book that has always made a big impression on me was {x548} by {x549}. I loved this author???s works because
            they taught me that {x550}.
            When I was young, I was told by {x551} that I should {x552}. They
            taught me this lesson
            when I was {x553}.
            To be able to work well with other people, one should be {x554}. It requires {x555} to build a lasting relationship.
            Success is something that {x556}. It does not {x557} and it is not
            {x558}.
            The secret to it would be {x559}. That is what I realized in my life on earth.
            CHARACTERISTICS OF A GOOD FRIEND?????
            One can only be considered a good friend if they are {x560}, {x561},
            and {x562}. If not, then there must be
            {x563}.
            What I value most about my family is the fact that {x564}. Even though there are hardships,
            we {x565} together.


            My life on earth has been emotionally {x566}, physically {x567}, and
            wholly {x568}. People have come
            and gone, seasons have changed countless times, and days have been numbered one by one. The single most important lesson
            I???ve learned in this {x569} world is that {x570}.
            The greatest advice I can give right now is that {x571}. I am hoping that people will listen and that my family will deem this as unforgettable and {x572}.
            PLEASE RECORD ANY OTHER INFORMATION YOU WISH TO SHARE """

        obj = Stroy(owner=request.user,
                    story_name='First Story', the_story=male)
        obj.save()
    return render(request, 'story/female.html')


def father_story(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        x5 = request.POST.get('x5')
        x6 = request.POST.get('x6')
        x7 = request.POST.get('x7')
        x8 = request.POST.get('x8')
        x9 = request.POST.get('x9')
        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')
        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')
        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')
        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')
        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')
        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')
        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')
        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')
        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')
        x100 = request.POST.get('x100')
        x101 = request.POST.get('x101')
        x102 = request.POST.get('x102')
        x103 = request.POST.get('x103')
        x104 = request.POST.get('x104')
        x105 = request.POST.get('x105')
        x106 = request.POST.get('x106')
        x107 = request.POST.get('x107')
        x108 = request.POST.get('x108')
        x109 = request.POST.get('x109')
        x110 = request.POST.get('x110')
        x111 = request.POST.get('x111')
        x112 = request.POST.get('x112')
        x113 = request.POST.get('x113')
        x114 = request.POST.get('x114')
        x115 = request.POST.get('x115')
        x116 = request.POST.get('x116')
        x117 = request.POST.get('x117')
        x118 = request.POST.get('x118')
        x119 = request.POST.get('x119')
        x120 = request.POST.get('x120')
        x121 = request.POST.get('x121')
        x122 = request.POST.get('x122')
        x123 = request.POST.get('x123')
        x124 = request.POST.get('x124')
        x125 = request.POST.get('x125')
        x126 = request.POST.get('x126')
        x127 = request.POST.get('x127')
        x128 = request.POST.get('x128')
        x129 = request.POST.get('x129')
        x130 = request.POST.get('x130')
        x131 = request.POST.get('x131')
        x132 = request.POST.get('x132')
        x133 = request.POST.get('x133')
        x134 = request.POST.get('x134')
        x135 = request.POST.get('x135')
        x136 = request.POST.get('x136')
        x137 = request.POST.get('x137')
        x138 = request.POST.get('x138')
        x139 = request.POST.get('x139')
        x140 = request.POST.get('x140')
        x141 = request.POST.get('x141')
        x142 = request.POST.get('x142')
        x143 = request.POST.get('x143')
        x144 = request.POST.get('x144')
        x145 = request.POST.get('x145')
        x146 = request.POST.get('x146')
        x147 = request.POST.get('x147')
        x148 = request.POST.get('x148')
        x149 = request.POST.get('x149')
        x150 = request.POST.get('x150')
        x151 = request.POST.get('x151')
        x152 = request.POST.get('x152')
        x153 = request.POST.get('x153')
        x154 = request.POST.get('x154')
        x155 = request.POST.get('x155')
        x156 = request.POST.get('x156')
        x157 = request.POST.get('x157')
        x158 = request.POST.get('x158')
        x159 = request.POST.get('x159')
        x160 = request.POST.get('x160')
        x161 = request.POST.get('x161')
        x162 = request.POST.get('x162')
        x163 = request.POST.get('x163')
        x164 = request.POST.get('x164')
        x165 = request.POST.get('x165')
        x166 = request.POST.get('x166')
        x167 = request.POST.get('x167')
        x168 = request.POST.get('x168')
        x169 = request.POST.get('x169')
        x170 = request.POST.get('x170')
        x171 = request.POST.get('x171')
        x172 = request.POST.get('x172')
        x173 = request.POST.get('x173')
        x174 = request.POST.get('x174')
        x175 = request.POST.get('x175')
        x176 = request.POST.get('x176')
        x177 = request.POST.get('x177')
        x178 = request.POST.get('x178')
        x179 = request.POST.get('x179')
        x180 = request.POST.get('x180')
        x181 = request.POST.get('x181')
        x182 = request.POST.get('x182')
        x183 = request.POST.get('x183')
        x184 = request.POST.get('x184')
        x185 = request.POST.get('x185')
        x186 = request.POST.get('x186')
        x187 = request.POST.get('x187')
        x188 = request.POST.get('x188')
        x189 = request.POST.get('x189')
        x190 = request.POST.get('x190')
        x191 = request.POST.get('x191')
        x192 = request.POST.get('x192')
        x193 = request.POST.get('x193')
        x194 = request.POST.get('x194')
        x195 = request.POST.get('x195')
        x196 = request.POST.get('x196')
        x197 = request.POST.get('x197')
        x198 = request.POST.get('x198')
        x199 = request.POST.get('x199')
        x200 = request.POST.get('x200')
        x201 = request.POST.get('x201')
        x202 = request.POST.get('x202')
        x203 = request.POST.get('x203')
        x204 = request.POST.get('x204')
        x205 = request.POST.get('x205')
        x206 = request.POST.get('x206')
        x207 = request.POST.get('x207')
        x208 = request.POST.get('x208')
        x209 = request.POST.get('x209')
        x210 = request.POST.get('x210')
        x211 = request.POST.get('x211')
        x212 = request.POST.get('x212')
        x213 = request.POST.get('x213')
        x214 = request.POST.get('x214')
        x215 = request.POST.get('x215')
        x216 = request.POST.get('x216')
        x217 = request.POST.get('x217')
        x218 = request.POST.get('x218')
        x219 = request.POST.get('x219')
        x220 = request.POST.get('x220')
        x221 = request.POST.get('x221')
        x222 = request.POST.get('x222')
        x223 = request.POST.get('x223')
        x224 = request.POST.get('x224')
        x225 = request.POST.get('x225')
        x226 = request.POST.get('x226')
        x227 = request.POST.get('x227')
        x228 = request.POST.get('x228')
        x229 = request.POST.get('x229')
        x230 = request.POST.get('x230')
        x231 = request.POST.get('x231')
        x232 = request.POST.get('x232')
        x233 = request.POST.get('x233')
        x234 = request.POST.get('x234')
        x235 = request.POST.get('x235')
        x236 = request.POST.get('x236')
        x237 = request.POST.get('x237')
        x238 = request.POST.get('x238')
        x239 = request.POST.get('x239')
        x240 = request.POST.get('x240')
        x241 = request.POST.get('x241')
        x242 = request.POST.get('x242')
        x243 = request.POST.get('x243')
        x244 = request.POST.get('x244')
        x245 = request.POST.get('x245')
        x246 = request.POST.get('x246')
        x247 = request.POST.get('x247')
        x248 = request.POST.get('x248')
        x249 = request.POST.get('x249')
        x250 = request.POST.get('x250')
        x251 = request.POST.get('x251')
        x252 = request.POST.get('x252')
        x253 = request.POST.get('x253')
        x254 = request.POST.get('x254')
        x255 = request.POST.get('x255')
        x256 = request.POST.get('x256')
        x257 = request.POST.get('x257')
        x258 = request.POST.get('x258')
        x259 = request.POST.get('x259')
        x260 = request.POST.get('x260')
        x261 = request.POST.get('x261')
        x262 = request.POST.get('x262')
        x263 = request.POST.get('x263')
        x264 = request.POST.get('x264')
        x265 = request.POST.get('x265')
        x266 = request.POST.get('x266')
        x267 = request.POST.get('x267')
        x268 = request.POST.get('x268')
        x269 = request.POST.get('x269')
        x270 = request.POST.get('x270')
        x271 = request.POST.get('x271')
        x272 = request.POST.get('x272')
        x273 = request.POST.get('x273')
        x274 = request.POST.get('x274')
        x275 = request.POST.get('x275')
        x276 = request.POST.get('x276')
        x277 = request.POST.get('x277')
        x278 = request.POST.get('x278')
        x279 = request.POST.get('x279')
        x280 = request.POST.get('x280')
        x281 = request.POST.get('x281')
        x282 = request.POST.get('x282')
        x283 = request.POST.get('x283')
        x284 = request.POST.get('x284')
        x285 = request.POST.get('x285')
        x286 = request.POST.get('x286')
        x287 = request.POST.get('x287')
        x288 = request.POST.get('x288')
        x289 = request.POST.get('x289')
        x290 = request.POST.get('x290')
        x291 = request.POST.get('x291')
        x292 = request.POST.get('x292')
        x293 = request.POST.get('x293')
        x294 = request.POST.get('x294')
        x295 = request.POST.get('x295')
        x296 = request.POST.get('x296')
        x297 = request.POST.get('x297')
        x298 = request.POST.get('x298')
        x299 = request.POST.get('x299')
        x300 = request.POST.get('x300')
        x301 = request.POST.get('x301')
        x302 = request.POST.get('x302')
        x303 = request.POST.get('x303')
        x304 = request.POST.get('x304')
        x305 = request.POST.get('x305')
        x306 = request.POST.get('x306')
        x307 = request.POST.get('x307')
        x308 = request.POST.get('x308')
        x309 = request.POST.get('x309')
        x310 = request.POST.get('x310')
        x311 = request.POST.get('x311')
        x312 = request.POST.get('x312')
        x313 = request.POST.get('x313')
        x314 = request.POST.get('x314')
        x315 = request.POST.get('x315')
        x316 = request.POST.get('x316')
        x317 = request.POST.get('x317')
        x318 = request.POST.get('x318')
        x319 = request.POST.get('x319')
        x320 = request.POST.get('x320')
        x321 = request.POST.get('x321')
        x322 = request.POST.get('x322')
        x323 = request.POST.get('x323')
        x324 = request.POST.get('x324')
        x325 = request.POST.get('x325')
        x326 = request.POST.get('x326')
        x327 = request.POST.get('x327')
        x328 = request.POST.get('x328')
        x329 = request.POST.get('x329')
        x330 = request.POST.get('x330')
        x331 = request.POST.get('x331')
        x332 = request.POST.get('x332')
        x333 = request.POST.get('x333')
        x334 = request.POST.get('x334')
        x335 = request.POST.get('x335')
        x336 = request.POST.get('x336')
        x337 = request.POST.get('x337')
        x338 = request.POST.get('x338')
        x339 = request.POST.get('x339')
        x340 = request.POST.get('x340')
        x341 = request.POST.get('x341')
        x342 = request.POST.get('x342')
        x343 = request.POST.get('x343')
        x344 = request.POST.get('x344')
        x345 = request.POST.get('x345')
        x346 = request.POST.get('x346')
        x347 = request.POST.get('x347')
        x348 = request.POST.get('x348')
        x349 = request.POST.get('x349')
        x350 = request.POST.get('x350')
        x351 = request.POST.get('x351')
        x352 = request.POST.get('x352')
        x353 = request.POST.get('x353')
        x354 = request.POST.get('x354')
        x355 = request.POST.get('x355')
        x356 = request.POST.get('x356')
        x357 = request.POST.get('x357')
        x358 = request.POST.get('x358')
        x359 = request.POST.get('x359')
        x360 = request.POST.get('x360')
        x361 = request.POST.get('x361')
        x362 = request.POST.get('x362')
        x363 = request.POST.get('x363')
        x364 = request.POST.get('x364')
        x365 = request.POST.get('x365')
        x366 = request.POST.get('x366')
        x367 = request.POST.get('x367')
        x368 = request.POST.get('x368')
        x369 = request.POST.get('x369')
        x370 = request.POST.get('x370')
        x371 = request.POST.get('x371')
        x372 = request.POST.get('x372')
        x373 = request.POST.get('x373')
        x374 = request.POST.get('x374')
        x375 = request.POST.get('x375')
        x376 = request.POST.get('x376')
        x377 = request.POST.get('x377')
        x378 = request.POST.get('x378')
        x379 = request.POST.get('x379')
        x380 = request.POST.get('x380')
        x381 = request.POST.get('x381')
        x382 = request.POST.get('x382')
        x383 = request.POST.get('x383')
        x384 = request.POST.get('x384')
        x385 = request.POST.get('x385')
        x386 = request.POST.get('x386')
        x387 = request.POST.get('x387')
        x388 = request.POST.get('x388')
        x389 = request.POST.get('x389')
        x390 = request.POST.get('x390')
        x391 = request.POST.get('x391')
        x392 = request.POST.get('x392')
        x393 = request.POST.get('x393')
        x394 = request.POST.get('x394')
        x395 = request.POST.get('x395')
        x396 = request.POST.get('x396')
        x397 = request.POST.get('x397')
        x398 = request.POST.get('x398')
        x399 = request.POST.get('x399')
        x400 = request.POST.get('x400')
        x401 = request.POST.get('x401')
        x402 = request.POST.get('x402')
        x403 = request.POST.get('x403')
        x404 = request.POST.get('x404')
        x405 = request.POST.get('x405')
        x406 = request.POST.get('x406')
        x407 = request.POST.get('x407')
        x408 = request.POST.get('x408')
        x409 = request.POST.get('x409')
        x410 = request.POST.get('x410')
        x411 = request.POST.get('x411')
        x412 = request.POST.get('x412')
        x413 = request.POST.get('x413')
        x414 = request.POST.get('x414')
        x415 = request.POST.get('x415')
        x416 = request.POST.get('x416')
        x417 = request.POST.get('x417')
        x418 = request.POST.get('x418')
        x419 = request.POST.get('x419')
        x420 = request.POST.get('x420')
        x421 = request.POST.get('x421')
        x422 = request.POST.get('x422')
        x423 = request.POST.get('x423')
        x424 = request.POST.get('x424')
        x425 = request.POST.get('x425')
        x426 = request.POST.get('x426')
        x427 = request.POST.get('x427')
        x428 = request.POST.get('x428')
        x429 = request.POST.get('x429')
        x430 = request.POST.get('x430')
        x431 = request.POST.get('x431')
        x432 = request.POST.get('x432')
        x433 = request.POST.get('x433')
        x434 = request.POST.get('x434')
        x435 = request.POST.get('x435')
        x436 = request.POST.get('x436')
        x437 = request.POST.get('x437')
        x438 = request.POST.get('x438')
        x439 = request.POST.get('x439')
        x440 = request.POST.get('x440')
        x441 = request.POST.get('x441')
        x442 = request.POST.get('x442')
        x443 = request.POST.get('x443')
        x444 = request.POST.get('x444')
        x445 = request.POST.get('x445')
        x446 = request.POST.get('x446')
        x447 = request.POST.get('x447')
        x448 = request.POST.get('x448')
        x449 = request.POST.get('x449')
        x450 = request.POST.get('x450')
        x451 = request.POST.get('x451')
        x452 = request.POST.get('x452')
        x453 = request.POST.get('x453')
        x454 = request.POST.get('x454')
        x455 = request.POST.get('x455')
        x456 = request.POST.get('x456')
        x457 = request.POST.get('x457')
        x458 = request.POST.get('x458')
        x459 = request.POST.get('x459')
        x460 = request.POST.get('x460')
        x461 = request.POST.get('x461')
        x462 = request.POST.get('x462')
        x463 = request.POST.get('x463')
        x464 = request.POST.get('x464')
        x465 = request.POST.get('x465')
        x466 = request.POST.get('x466')
        x467 = request.POST.get('x467')
        x468 = request.POST.get('x468')
        x469 = request.POST.get('x469')
        x470 = request.POST.get('x470')
        x471 = request.POST.get('x471')
        x472 = request.POST.get('x472')
        x473 = request.POST.get('x473')
        x474 = request.POST.get('x474')
        x475 = request.POST.get('x475')
        x476 = request.POST.get('x476')
        x477 = request.POST.get('x477')
        x478 = request.POST.get('x478')
        x479 = request.POST.get('x479')
        x480 = request.POST.get('x480')
        x481 = request.POST.get('x481')
        x482 = request.POST.get('x482')
        x483 = request.POST.get('x483')
        x484 = request.POST.get('x484')
        x485 = request.POST.get('x485')
        x486 = request.POST.get('x486')
        x487 = request.POST.get('x487')
        x488 = request.POST.get('x488')
        x489 = request.POST.get('x489')
        x490 = request.POST.get('x490')
        x491 = request.POST.get('x491')
        x492 = request.POST.get('x492')
        x493 = request.POST.get('x493')
        x494 = request.POST.get('x494')
        x495 = request.POST.get('x495')
        x496 = request.POST.get('x496')
        x497 = request.POST.get('x497')
        x498 = request.POST.get('x498')
        x499 = request.POST.get('x499')
        x500 = request.POST.get('x500')
        x501 = request.POST.get('x501')
        x502 = request.POST.get('x502')
        x503 = request.POST.get('x503')
        x504 = request.POST.get('x504')
        x505 = request.POST.get('x505')
        x506 = request.POST.get('x506')
        x507 = request.POST.get('x507')
        x508 = request.POST.get('x508')
        x509 = request.POST.get('x509')
        x510 = request.POST.get('x510')
        x511 = request.POST.get('x511')
        x512 = request.POST.get('x512')
        x513 = request.POST.get('x513')
        x514 = request.POST.get('x514')
        x515 = request.POST.get('x515')
        x516 = request.POST.get('x516')
        x517 = request.POST.get('x517')
        x518 = request.POST.get('x518')
        x519 = request.POST.get('x519')
        x520 = request.POST.get('x520')
        x521 = request.POST.get('x521')
        x522 = request.POST.get('x522')
        x523 = request.POST.get('x523')
        x524 = request.POST.get('x524')
        x525 = request.POST.get('x525')
        x526 = request.POST.get('x526')
        x527 = request.POST.get('x527')
        x528 = request.POST.get('x528')
        x529 = request.POST.get('x529')
        x530 = request.POST.get('x530')
        x531 = request.POST.get('x531')
        x532 = request.POST.get('x532')
        x533 = request.POST.get('x533')
        x534 = request.POST.get('x534')
        x535 = request.POST.get('x535')
        x536 = request.POST.get('x536')
        x537 = request.POST.get('x537')
        x538 = request.POST.get('x538')
        x539 = request.POST.get('x539')
        x540 = request.POST.get('x540')
        x541 = request.POST.get('x541')
        x542 = request.POST.get('x542')
        x543 = request.POST.get('x543')
        x544 = request.POST.get('x544')
        x545 = request.POST.get('x545')
        x546 = request.POST.get('x546')
        x547 = request.POST.get('x547')
        x548 = request.POST.get('x548')
        x549 = request.POST.get('x549')
        x550 = request.POST.get('x550')
        x551 = request.POST.get('x551')
        x552 = request.POST.get('x552')
        x553 = request.POST.get('x553')
        x554 = request.POST.get('x554')
        x555 = request.POST.get('x555')
        x556 = request.POST.get('x556')
        x557 = request.POST.get('x557')
        x558 = request.POST.get('x558')
        x559 = request.POST.get('x559')
        x560 = request.POST.get('x560')
        x561 = request.POST.get('x561')
        x562 = request.POST.get('x562')
        x563 = request.POST.get('x563')
        x564 = request.POST.get('x564')
        x565 = request.POST.get('x565')
        x566 = request.POST.get('x566')
        x567 = request.POST.get('x567')
        x568 = request.POST.get('x568')
        x569 = request.POST.get('x569')
        x570 = request.POST.get('x570')
        x571 = request.POST.get('x571')
        x572 = request.POST.get('x572')
        x580 = request.POST.get('x580')
        x581 = request.POST.get('x581')
        male = f"""I was born on the {x1} in {x2}, a city in {x3} at {x4} hospital.
            My full name is {x5} .

            The people who decided on this name are {x6}.
            I was named this way because {x7}.Sometimes, I go by the nickname {x8} which I got from {x9}.
            I have a beautiful mother named {x10}. She was born on {x11} in {x12}.
            The place she grew up in {x13} was lovely just like her.
            Meanwhile, my father, {x14}, was born on the {x15}. He was raised in
            the city of {x16}.


            To complete my family, I have {x17} siblings.
            Their names are {x18}. They were born in {x19}. My mother gave birth
            to {20} on {x21}. On the other hand,
            {x22} was born on {x23}.
            I have a beautiful/handsome sister/brother who goes by the name {x24}. She/he was born on the
            {x25} in
            {x26}.
            My mother was raised well by her parents, {x7} and {x27}. My
            grandmother was named {x28}. Her birthday was on
            the {x29}; whereas, my grandpa, {x30}, was born on {x31} in the village of {x32}.


            On my father???s side, I was blessed with the lives of my grandma, {x33}, and my grandpa, {x34}.
            Granny was born on {x35} in {x36}. My grandfather???s birth date,
            however, was on {x37}. His family
            gleefully welcomed him on this day in the city of {x38}.



            I have the most gorgeous wife. She was named {x39} but I call her {x40}. I am thankful that she was successfully given
            birth to on the{x41} in the wonderful city of {x42}.

            {x43} and I were blessed with {x44} children who we named as {x45}.
            {x46} was born on {x47} in {x48}. On the
            other hand, {x49}???s birthdate is on {x50}. My wife gave
            birth to him/her in {x51}.



            Over the years, my children grew up and had their own kids, too. My adorable grandkids are named {x580} and {x581}.
            The first one is born in {x52} on the {x53}.
            {x54} was born on {x55} in the city of {x55}.



            I spend most of my free time {x56} while drinking {x57}.


            My most favorite sport is {x58} because I think it is {x59}


            My go-to vacation spot is {x61}. I find it {x62}.


            The meal that I enjoy the most is {x63}.


            My favorite song is called {x64}; it is sung by {x65}. The reason why
            I love it is that it reminds me of
            {x67}.


            Currently, my favorite television show is {x68}. Back then, I really loved the series {x69}.



            I have watched the movie {x70} several times already and I never get tired of it because it is
            {x71}.


            My hobbies are {x72}, {x73}, and {x74}. On
            the weekends, I also {x75} with my {x76}.



            The social gatherings that I usually enjoy are {x77}.


            My greatest talent is {x78}. I have used it in many ways throughout my life such as when I
            {x79}.


            The best characteristic that I love about myself is my {x80}.

            Sometimes, I wish I could stop being {x81}.



            Currently, I am living a {x81} life here in {x82} with my {x83}.
            On the weekdays, I spend most of my time {x84}. By the end of the day, I would feel {x85} and {x86}.



            I grew up in a {x87} neighborhood where I met various interesting people like {x88}.
            Remembering it, I can say that it was actually a {x89} place.


            My childhood home was {x90}. I enjoyed all of the {x91} mornings and
            {x92} nights in it. The house was
            suitable for a family of {x93} people. My time there was {x94}.



            My favorite place in this {x95} house was the {x96}. It had a special
            place in my heart because it {x97}.




            When I was younger, I had to do chores like {x98}.


            ({x99}) I got a daily/weekly/monthly allowance worth {x100}.



            The indoor activity that I enjoyed the most was {x101}. This was because {x102}.


            Back then, I really enjoyed {x103} outside the house.


            As a child, I was particularly skilled at {x104}.



            I also had some toys that cheered me up on sad days. These are {x105}.



            I had a special place that I called ???mine.??? It was this {x106} space filled with {x107}. I used to {x108} a lot when
            I stayed here.


            As a child, I always anticipated going out to {x109}.



            Being a boy, I {x110} not enjoy reading.
            (If yes) I liked collecting {x111} books!


            of this experience???{x112}
            I lived in a {x113} (Religious/Non-Religious) family.
            (If religious). I attended a church called {x114} which was located in {x115}. I remember the times when I {x116}.

            I {x117} baptized or dedicated as an infant.
            (If baptized) As an infant, I was baptized by {x118} in {x119}. My
            {x120} attended the celebration



            Some of the childhood experiences that helped me become who I am right now are {x121}.



            I remember having a childhood friend named {x122}. He/she was very {x123} and we had a {x124} time together.



            From my childhood, I will be eternally grateful for the {x125}. Because of it, I grew up to be
            a {x126} person.
            Family LIFE
            50 A family is a circle of love?????formed by memories,??filled with devotion.????



            My favorite memory with my dad was when {x127}. This is a special event for me because {x128}.



            My father???s insights on life and its adventures was {x129}. This made me become more {x130} regarding my own life.


            My father and I used to {x131} together and I really enjoyed it because {x132}.


            I think I have grown up to be like my father when it comes to my {x133}. I always think that I
            got this from him.


            One thing my dad always said was {x134}. I believe that this is actually a great {x135} and it helped me
            establish myself.


            My father worked as a/an {x136}. This job piqued / did not pique my interest because {x137}.


            One of the most memorable things about my mother from when I was a little boy was how she {x138}. This is because {x139}.

            My mom always had a {x140} outlook towards life. This attitude of hers affected me in a way
            that I became more {x141}.



            I am similar to her because she is {x142} just like me. My mother is the most {x143} woman I have ever met and I love her
            for it.


            Back when I was a child, I really liked {x144} with my mom. Until now, I still feel {x145} whenever I remember this.




            My mother???s occupation was {x146}. This helped me decide on my future career because I found it
            {x147} how she
            {x148}.


            My family was {x149}. We encountered problems such as {x150} and it
            was hard for me growing up. But
            I am now {x151} about my life. These circumstances have made me {x152}
            and {x153}.

            As I was growing up, my parents requested that I {x154}.


            This formed my mindset regarding parenting. In complete honesty, I actually require my children to {x155}, similar to /
            different from the obligations I had as a kid.


            Some of the qualities that my parents nurtured in me are my characteristics of being {x156} and
            {x157}. I am thankful for these.



            My parents always told me to be a {x158} person. Of course, I valued their encouragement
            because I loved them.



            I also loved my siblings/sister/brother so much. My fondest memories of them/him/her was that time when {x159}.

            Of course, being young means you get to enjoy the beauty of life without heavily thinking of the consequences. I played
            around with my
            siblings/brother/sister and we used to {x160}. It was funny for me back then but looking back,
            I think {x161}.
            My siblings/brother/sister and I were {x162}. We had {x163} days
            together.
            In addition to our lovely family, we had a pet {x164} / pets named {x165}. He/she/they were adorable!
            The thing I loved most about having {x166} growing up with me was {x167}. I loved {x168} with {x169}!
            On regular days, my family {x170} together. In the summer, we would often go {x171}. But most especially,
            we loved spending time together, either by {x172} or {x173}.
            My early memories of my grandparents was how they {x174}. My grandma would always {x175} while my grandpa {x176}.

            They lived in a lovely place in {x177}. Around their area, there were many {x178}. It was a {x179} neighborhood.
            My grandmother worked as a {x180} and my grandpa did some {x181} job.

            Whenever my family visited them / whenever they visited us, I remember that we always had an amazing time together. My
            grandma and
            grandpa prepares a delicious meal for us. Their {x182} was my favorite!

            I loved being with my grandparents because they were {x183}. I always watched them {x184} . They cared for me and my
            siblings/brother/sister.
            A valuable lesson that I learned from being with them was that {x185}. Aside from this, I was
            also inspired by them to be a {x186}
            person.
            The only things I remember about my great-grandparents are that they {x187}.
            I believe that my ancestors were {x188} and that I might have a/an {x189} origin.
            My favorite home-cooked meal was {x190} because it was honestly delicious and {x191}! It reminds me of {x192}.
            Whenever my family and I {x193} together, we would always prepare {x194}.
            We used to go out for dinner frequently/sometimes. When we do, I would always request that we go to {x195} or try other restaurants
            that serve {x196}.
            (Yes) Our house was a great place for celebrations. I remember having company often. My family???s friends or some of our
            other relatives
            would always come to visit or {x197} with us.
            (No) Although we were a happy family, we did not often have company perhaps because our place was {x198}.
            My family outings were {x199}! We would always go to {x200} and {x201} together. Holidays are my {x202} favorite season!
            In the winter, I remember {x203} with my siblings/brother/sister. As a whole family, we liked
            playing {x204}. My favorite
            winter food was {x205}. And drinks? Of course, {x206}.
            Family reunions are {x207} for me. I enjoyed {x208} whenever we held
            one.
            (No) I was not really close to my relatives.
            (Yes) I had close relationships with my other relatives especially with my {x209}. I am happy
            about these because I could always
            {x210} to them whenever I am {x211}.

            Every time I think about my family, the first thing that comes to mind was {x212}. I feel like
            I associated them with it because of
            the {x213} they bring to my life.

            Knowledge is the power??that gives us wings to soar.??

            I attended elementary at {x214} in {x215}. I often rode the {x216} to school and back OR I often biked/walked to
            school alone/with my {x217}.My earliest memories of going to {x218} was that I would always {x219}
            in {x220} Class. I also remember hanging out
            with my childhood friends named {x221} and {x222}.
            92 WHAT DID YOU ENJOY?? MOST ABOUT ELEMENTARY SCHOOL?????
            One thing I loved most about elementary was {x223} on {x224} days.
            But, I really hated that I had to {x225}.
            Next, I attended middle school at {x226}. Every day, I would go there via {x227}. Sometimes, I would {x228}.
            When I was in high school, I attended {x229}. It was a very {x230}
            school and I met a lot of {x231} people there.
            My favorite subjects in middle school were {x232} and {x233} because
            {x234}.
            Meanwhile, in high school, I really liked going to {x235} class. The teacher was really {x236} and my classmates were
            {x237}.
            Some extracurricular activities that I enjoyed the most were {x238}. I chose these because
            {x239}.
            Over the years, I have received some special awards such as {x240}.
            I had a favorite teacher whose name was {x241}. I can say that she/he had a big influence on
            shaping who I am now by {x242}.
            Back when I was still in school, there were many fashion trends that arose such as {x243}.
            (Yes) I participated in them because {x244}.
            (No) I did not participate much when it comes to these because {x245}.
            The most popular songs that I remember around the time I was studying were {x246}. I really
            {x247} this kind of music.
            Meanwhile, the highest grossing movies were {x248}. People {x249}
            these so much!
            The television shows that were much awaited were {x250}.
            Lastly, celebrities such as {x251} were having their primes then.
            The parties that I attended were mostly {x252}. Some of the party-goers were from {x253}. I can still remember
            how {x254} the crowd was.
            (No) I didn???t have a car when I was in high school but if I did it probably would be a __________.
            (Yes) I had a car when I was a teenager and it was a {x255}. I was {x256} about how it looks like.
            I really went places with that car.
            My middle school and high school years were a bit difficult because of {x257}. But, as a whole
            I think I really {x258}
            my teenage years.
            DURING YOUR MIDDLE SCHOOL AND HIGH SCHOOL YEARS???
            I am happy that I got to {x259} while I was schooling. It was a great privilege for me.
            change with time?????
            During this time, I was thinking about my goal of becoming a {x260} and I really hoped to
            achieve my dreams such as
            that of {x261}. Over time, I continued/stopped inching towards these goals.
            After graduation, I chose to follow the path of becoming a {x262}.
            I went to college / a career training school called {x263} in the city of {x264}. I took up a degree in the field of
            {x265}.
            I had to move away from home to continue studying and it was {x266}. I was looking forward to
            {x267} but I really felt
            {x268} when I was away from my family.
            I lived in an apartment/dorm nearby. It was {x269}, {x270}, and {x271}. I had a {x272} time studying when I was
            there.
            (with roommate) I had a roommate whose name was {x273}. He/she was a {x274} person.
            My most favorite college memories were the one at {x275} with my {x276}. Those experiences were {x277}
            and unforgettable.
            On??the Job??

            Any job can be made great.??It???s the worker???not the work?????that counts

            When I was young, I tried to gain money by {x278}. My earnings were used to pay for my {x279}.


            My first career-oriented job after graduation was a {x280} at {x281}.
            Here, I would be the one responsible for
            {x282}.
            When I found out that I got accepted in this job, I was very {x283}. I thought that this can
            help me in {x284}.
            The one thing I love most about my first job was {x285}. The environment in the workplace was
            also {x286}.
            Among the jobs that I tried and had in the past, the one in which I probably had the most fun was when I was working at
            {x287}
            as a {x288}. This is due to the fact that {x289}.

            Meanwhile, the worst job was in {x290}. I mostly did not enjoy working here because of {x291}.
            The most rewarding out of all, however, was the job at {x292}. This is because I was {x293}. I really love
            {x294} about this job.
            Of course, some opportunities can only be achieved when you move out of your comfort zone. As for me, I had to move away
            when I
            was working at {x295} in {x296}. I felt {x297} because of it but I am {x298} that I took it.
            For some jobs, I had to go places for {x299} events. The most memorable place I visited while
            doing so was a {x300} in {x301}.
            I had a coworker / superior who displayed the role of a friendly and trustworthy mentor to me. His/her name was {x302} and
            he/she taught me how to {x303}.
            (If yes) Over the years, I was able to be a mentor to others, too. I believe it was a {x304}
            experience for me.
            (If no) I might not have been an official mentor to others myself, but I believe that I was also able to help my
            colleagues in various ways.

            At work, I met all types of people but I found {x305} friends, too.
            When I???m just at home, I like to work on {x306}.
            But, I usually avoid doing {x307} because {x308}.
            Love??AND??Marriage????
            130 When love touches our hearts,??happiness fills our days.??

            I remember having a crush on {x309} when I was younger. I believe she was the first person I
            truly admired.
            The first boy party that I attended was when I was {x310} years old. It was held at {x311}..
            My first kiss was {x312}. I remember how I felt really {x313}
            afterwards.
            My first ever date was {x314}. It went {x315}. I had a {x316} time with {x317}.
            When that happened, lovers usually {x318} when they went out together and hung out. The kind of
            date nights was very {x319}
            compared to now.
            I met my lovely wife when I was {x320} years old.


            I will be eternally grateful that our paths crossed on {x321} in {x322}. If it weren???t for the {x323},
            I wouldn???t have seen her.
            She was {x324}, {x325}, and {x326}. Those
            qualities really captured my attention.
            Initially, I thought that she was {x327}. Over time, I realized how {x328} my first impression was compared to how
            she really is.
            I courted her for {x329} months. She was definitely worth the wait.
            When we just started dating, we really loved {x330} together. Some other things that we enjoyed
            doing were {x331}
            and {x332}.
            I knew she was the one when {x333} after I realized that she could be {x334}.
            The marriage proposal was {x335} and I am sincerely {x336} about it!
            There were {x337} everywhere while I
            was waiting for her response.
            We officially tied the knot on {x338} at a {x339} in {x340}.


            I wore a {x341}.

            While she wore a beautiful and {x342} wedding dress/gown.??

            It was a small/big wedding. We had about {x343} guests.

            For our first dance as husband and wife, we swayed to the song entitled {x344} which was chosen
            because {x345}.
            The most remarkable memory of mine from that special day was {x346}.

            Recall a special moment or event from the honeymoon.??
            Our honeymoon was {x347}! We went to {x348} wherein we {x349}. What I loved most about this
            experience was the fact that {x350}.


            After getting married, we lived in {x351}. I clearly remember how {x352} our home was.


            Early into our marriage, we had {x353} nights where we would enjoy dinner together over a
            {x354}.
            We started thinking about having children when {x355}. I really looked forward to {x356} and seeing my wife
            {x357} for our kids.


            WHEN YOU WERE FIRST MARRIED???What were some of the fun things you did with them???
            As a couple, we had some close friends. The ones that we mostly hung out with were named {x358}.
            We would always {x359} together and it felt {x360}! I {x361} spending time with them.


            {x362} and I really loved {x363} whenever we had free time. Aside from
            this, we also enjoyed {x364}.
            For me, marriage has been rewarding because {x365}.
            To be able to withstand any hardship, I believe that the most important key to a healthy marriage is {x366}.
            Of course in our marriage we also had hard times wherein we needed to be there for each other more. These instances that
            required
            sharing and companionship happened when {x367}.
            My daily relationship with my loving wife has been {x368}. Right now, my favorite thing about
            being married to is {x369}.
            Parenting????
            To be a father is to protect,??nurture, and guide,??but most of all, to love.????


            When I found out that I was going to be a dad, I felt {x370}. I remember that day being a
            {x371}
            one.
            I lived in {x372}
            My FIRST CHILD WAS BORN on ??{x373}
            My growing family then lived at a {x374} in {x375}.


            Back then, our situation was {x376}.
            We had problems such as {x377} OR We did not have any problems.


            Every time I looked at my firstborn when he/she was an infant, I felt {x378}. Every day with
            him/her was really
            {x379}.


            Becoming a father was {x380}. It caused me to have a more {x381}
            outlook on life. I realized that {x382}.
            168 WHAT IS YOUR MOST VIVID MEMORY??OF YOUR CHILDREN???S EARLY YEARS?????
            I have some crystal clear memories of my children when they were still young. These include the time when {x383} and
            also that instance when {x384}.


            Back then, I really enjoyed {x386} with them. When they grew up a bit, we would always {x385}.
            Of course, there had to be some days that I would need to spend alone with my wife. Whenever we took the days off for
            our special dates,
            we would {x387}.

            As a parent, I believe that it is undeniable that I have similarities with my kids. These include {x388}.
            As for them, my kids are similar in a way that they are all {x389}. This might be because
            {x390}.
            My spouse and I tried to instill the qualities of being {x391}, {x392}, and {x393} to our kids.
            I know that I have been blessed to be a father because I get to experience {x394}. This is what
            I consider my greatest joy
            in this {x395} role.
            Because life is not perfect, our family had problems, too. The greatest challenge that I experienced as a dad to {x396} beautiful kids
            was {x397}.
            I was raised in a {x398} family which is similar/different to my children???s upbringing. They
            grew up in a {x399} house, a
            {x400} neighborhood, with {x401} parents.
            THAT YOU WISH YOU???D KNOWN WHEN YOU??FIRST BECAME A FATHER?????
            Sometimes, I wish that I knew better when I became a father to my firstborn. One thing that I learned through time that
            I could
            have known back when I was raising {x402} was {x403}.
            I am a {x404} person. Somehow I wish my kids can grow up to be {x405}
            -- opposite/similar to me.
            Being a father taught me a lot of {x406} lessons but to me the most important thing among all
            these is {x407}.
            This is due to the fact that {x408}.


            Life offers so many??wonderful things to share,??so many special joys to celebrate.????

            We would always {x409} on my birthday when I was young. The guests were usually {x410}. It was a {x411}
            celebration.


            My favorite memory of a birthday party was when {x412}. This happened on my {x413} th birthday.
            The most special presents that I ever received are {x414}. For me, they were wonderful because
            {x415}.
            I often requested that my parents cook/make/buy {x416} to serve on my birthdays. I really loved
            these food because
            {x417}.
            Apart from the celebration of my birth, I had other unique parties held at our humble abode. These include {x418}.
            The ambiance of the surroundings during this feast was {x419}. Guests had to wear {x420}.
            As a child, my favorite religious festivity is {x421}. We would {x422}
            together as a family and {x423}.
            We prepare meals such as {x424} to feast on.
            Among these types of celebrations, the main thing that stands out in my memory is {x425} due to
            the fact that
            {x426}.

            I really liked the {x427} that we buy/make during my childhood. It tasted {x428} and {x429}.
            My favorite christmas carol was {x420}. Right now, {x431} is my
            favorite.
            where??it??came??from?????
            What my family told us about Santa Claus was that he was/wasn???t real. I always knew/didn???t know where the gifts from my
            Christmas
            stocking / ornament came from.
            During these holidays, we often gave presents to each other. My most loved gift was the {x432}
            from my {x433}
            because {x434}.
            Meanwhile, the most memorable present that I gave someone was a {x435}. This was for my {x436}.
            I still remember how he/she {x437} it.
            Growing up, I always loved the religious tradition we had in our family. Now that I have my own, I continued to {x438}.
            As a parent, the most meaningful Christmas for me was when {x439} because {x440}.
            195 HOW DID YOU CELEBRATE THANKSGIVING???Did you have a favourite Thanksgiving tradition?????
            For Thanksgiving, my family usually {x441}. The tradition that I love most is {x442}.
            Preparing and eating Thanksgiving food is also {x443}.
            When I was a kid, I really {x444} Australia day. The neighborhood would always be {x445} and there were {x446}
            everywhere!
            What was your favourite Halloween treat?????
            I did/didn???t really enjoy halloween. I remember an especially fun costume worn by {x447}. It
            was a {x448}.
            I also {x449} to trick-or-treat! My favorite treat was {x450} since
            {x451}. One memory that I have of a really enjoyable holiday celebration was when {x452}. It happened around the time that {x453}. I think it was a meaningful experience for me because {x454}.
            Moment by moment,??day by day,??families create a lifetime of memories.??The happiest time of my life, I must say, is when {x455}. I cannot explain the joy that I felt because {x456}. To me, it???s an experience that cannot be beaten by anything else. Meanwhile, the saddest for me was when {x457}. I believe I had a {x458} time moving on from this
            because {x459}. Over the years, I had many commitments and responsibilities but there was a time wherein I was always occupied.
            The busiest I have ever been was when {x460}. It was due to the fact that {x461}. On the other hand, I had relaxing days, too, but I am confident to say that I was most comfortable and at ease when
            {x462}. A life-changing event that really influenced me in many ways was when {x463}. Somehow, it
            helped me {x464}. One political event that I participated in or witnessed over the years was {x465}. It made a
            really strong impression on for the reason that {x466}.  (I have) I served in the military back then. It was a {x467} experience, while at the same
            time, there were instances that {x468} me such as {x469}. (Other family members have) Some of my relatives had to serve in the military. I was really {x470} about it and it
            often {x471} me thinking about what was happening to them while in there.
            I can proudly say that I was able to {x472}. This had been fulfilling for me because {x473}.
            I have been in an accident/major surgery/long illness. This involved me being {x474}.
            It sincerely didn???t have / had a lasting effect on me because it made me {x475}.
            My family experienced a tragic time when {x476} happened. I have always been a {x477} person and although I was
            {x478}, I made sure that I would still be able to {x479}.
            YOU HAD TO MAKE IN YOUR LIFE???HAD TO MAKE IN YOUR LIFE???Would you make the same choice again?????
            The most difficult choice that I made was {x480}. I do not regret / regret it until now and if
            I would be given a chance to choose a different option, I would {x481}. Throughout the years, I really didn???t travel much / went to a lot of places but the most memorable experience I had
            while traveling was when I went to {x482} alone / with {x483}. There, I / we did
            activities such as {x484}. The first time I rode an airplane was when I was off to {x485} when I was {x486} years old. I had to go there because of
            {x487}. (No) I did not get the chance to travel abroad but I bet I would love to see {x488}.
            (Yes) I had the opportunity of traveling abroad and it was {x489}! I enjoyed {x490} because {x491}.
            Among all the tourist spots and vacation places that I have been to, I can say that the most interesting and exciting
            was when I went
            to {x492}. It was special because {x493}.
            I {x494} helping people because I believe that {x495}. One person that
            I extended my helping hands to was named {x496}.
            He/she needed assistance in {x497} so I {x498}.
            I also dedicated myself to a cause / organization for the {x499}. I participated in it with an
            open heart because {x500}.
            How did you benefit from it???
            I was also given the chance to join competitive activities like {x501} which helped me grow in
            a way that {x502}.
            Being on earth for {x503} years is a lot of work and over the years I did many {x504} things. Thankfully, my efforts were
            professionally recognized when I {x505}. Upon receiving my award, I felt {x506}.
            The most important invention in my lifetime was {x507}. I will be eternally grateful that it
            existed because
            {x508}.
            Some of the most remarkable political / international events that I witnessed or participated in while I am living were
            {x509}.
            These were memorable because {x510}.
            Science has always {x511} me but, in particular, {x512} piqued my
            interest.
            Growing up to be who I am today and comparing my upbringing to the youth of the current times, I can say that we are
            very
            similar / different in ways such as {x513}. This might be due to the fact that {x514} nowadays
            compared to back then.
            Even though I was {x515}, I don???t think I would want to change that about how I lived my life
            even if I would be given a chance to do
            so.
            Although, I guess I would have changed {x516} because {x517}.
            In the next ten years, I wish my family will become {x518} so that {x519}.
            For the world to be a better and happier place however, I hope that {x520} will change and
            {x521}
            can be more {x522}.
            Inspiration????How great it is??to have the freedom to dream??and the opportunity??to make those dreams come true.??

            The people I would like to thank for helping me be the person I am today are {x523}. They
            helped me
            {x524}.
            Whenever I needed help, I would always approach {x525} and he/she always had the answers that
            could make me {x526}.
            (No) Religion did not really play a significant role in my life.
            (Yes) Religion helped me be a {x527} person. I relied on my faith every time I {x528}.
            A poem/passage/quote that I learned to live by or admired sincerely was {x529} by {x530}. This is due to the fact that
            {x531}.
            If worst comes to worst and I am only allowed to keep a single family photo, it would be that of {x532}. This is {x533}
            for me because it reminds me of {x534}.
            Perhaps, the greatest possession that I have is my {x535}. It is unbeatable by any other
            because {x536}.
            The greatest gifts in my life are {x537}. I will forever be grateful for these.
            (No) I never felt that I was born to become someone.
            (Yes) I have always felt that I was born to be {x538} -- that I was called to {x539}.
            Back when I was little, I looked up to {x540} the most because {x541}.
            Somehow, I grew up to be
            closely similar to/different from them.
            A celebrity that I admired was {x542} because of his/her {x543}.
            If not, who would you like to hear and why?????
            (No) I have never been able to listen to a public speaker but if I would be given the chance, I want to hear {x544} because he/she
            {x545}.
            (Yes) I was able to witness {x546} speaking live and it greatly impacted me in a way that
            {x547}.

            What are some of the insights that you???ve received?????
            One book that has always made a big impression on me was {x548} by {x549}. I loved this author???s works because
            they taught me that {x550}.
            When I was young, I was told by {x551} that I should {x552}. They
            taught me this lesson
            when I was {x553}.
            To be able to work well with other people, one should be {x554}. It requires {x555} to build a lasting relationship.
            Success is something that {x556}. It does not {x557} and it is not
            {x558}.
            The secret to it would be {x559}. That is what I realized in my life on earth.
            CHARACTERISTICS OF A GOOD FRIEND?????
            One can only be considered a good friend if they are {x560}, {x561},
            and {x562}. If not, then there must be
            {x563}.
            What I value most about my family is the fact that {x564}. Even though there are hardships,
            we {x565} together.


            My life on earth has been emotionally {x566}, physically {x567}, and
            wholly {x568}. People have come
            and gone, seasons have changed countless times, and days have been numbered one by one. The single most important lesson
            I???ve learned in this {x569} world is that {x570}.
            The greatest advice I can give right now is that {x571}. I am hoping that people will listen and that my family will deem this as unforgettable and {x572}.
            PLEASE RECORD ANY OTHER INFORMATION YOU WISH TO SHARE """

        obj = Stroy(owner=request.user,
                    story_name='First Story', the_story=male)
        obj.save()
    return render(request, 'story/father.html')


def mother_story(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        x5 = request.POST.get('x5')
        x6 = request.POST.get('x6')
        x7 = request.POST.get('x7')
        x8 = request.POST.get('x8')
        x9 = request.POST.get('x9')
        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')
        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')
        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')
        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')
        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')
        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')
        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')
        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')
        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')
        x100 = request.POST.get('x100')
        x101 = request.POST.get('x101')
        x102 = request.POST.get('x102')
        x103 = request.POST.get('x103')
        x104 = request.POST.get('x104')
        x105 = request.POST.get('x105')
        x106 = request.POST.get('x106')
        x107 = request.POST.get('x107')
        x108 = request.POST.get('x108')
        x109 = request.POST.get('x109')
        x110 = request.POST.get('x110')
        x111 = request.POST.get('x111')
        x112 = request.POST.get('x112')
        x113 = request.POST.get('x113')
        x114 = request.POST.get('x114')
        x115 = request.POST.get('x115')
        x116 = request.POST.get('x116')
        x117 = request.POST.get('x117')
        x118 = request.POST.get('x118')
        x119 = request.POST.get('x119')
        x120 = request.POST.get('x120')
        x121 = request.POST.get('x121')
        x122 = request.POST.get('x122')
        x123 = request.POST.get('x123')
        x124 = request.POST.get('x124')
        x125 = request.POST.get('x125')
        x126 = request.POST.get('x126')
        x127 = request.POST.get('x127')
        x128 = request.POST.get('x128')
        x129 = request.POST.get('x129')
        x130 = request.POST.get('x130')
        x131 = request.POST.get('x131')
        x132 = request.POST.get('x132')
        x133 = request.POST.get('x133')
        x134 = request.POST.get('x134')
        x135 = request.POST.get('x135')
        x136 = request.POST.get('x136')
        x137 = request.POST.get('x137')
        x138 = request.POST.get('x138')
        x139 = request.POST.get('x139')
        x140 = request.POST.get('x140')
        x141 = request.POST.get('x141')
        x142 = request.POST.get('x142')
        x143 = request.POST.get('x143')
        x144 = request.POST.get('x144')
        x145 = request.POST.get('x145')
        x146 = request.POST.get('x146')
        x147 = request.POST.get('x147')
        x148 = request.POST.get('x148')
        x149 = request.POST.get('x149')
        x150 = request.POST.get('x150')
        x151 = request.POST.get('x151')
        x152 = request.POST.get('x152')
        x153 = request.POST.get('x153')
        x154 = request.POST.get('x154')
        x155 = request.POST.get('x155')
        x156 = request.POST.get('x156')
        x157 = request.POST.get('x157')
        x158 = request.POST.get('x158')
        x159 = request.POST.get('x159')
        x160 = request.POST.get('x160')
        x161 = request.POST.get('x161')
        x162 = request.POST.get('x162')
        x163 = request.POST.get('x163')
        x164 = request.POST.get('x164')
        x165 = request.POST.get('x165')
        x166 = request.POST.get('x166')
        x167 = request.POST.get('x167')
        x168 = request.POST.get('x168')
        x169 = request.POST.get('x169')
        x170 = request.POST.get('x170')
        x171 = request.POST.get('x171')
        x172 = request.POST.get('x172')
        x173 = request.POST.get('x173')
        x174 = request.POST.get('x174')
        x175 = request.POST.get('x175')
        x176 = request.POST.get('x176')
        x177 = request.POST.get('x177')
        x178 = request.POST.get('x178')
        x179 = request.POST.get('x179')
        x180 = request.POST.get('x180')
        x181 = request.POST.get('x181')
        x182 = request.POST.get('x182')
        x183 = request.POST.get('x183')
        x184 = request.POST.get('x184')
        x185 = request.POST.get('x185')
        x186 = request.POST.get('x186')
        x187 = request.POST.get('x187')
        x188 = request.POST.get('x188')
        x189 = request.POST.get('x189')
        x190 = request.POST.get('x190')
        x191 = request.POST.get('x191')
        x192 = request.POST.get('x192')
        x193 = request.POST.get('x193')
        x194 = request.POST.get('x194')
        x195 = request.POST.get('x195')
        x196 = request.POST.get('x196')
        x197 = request.POST.get('x197')
        x198 = request.POST.get('x198')
        x199 = request.POST.get('x199')
        x200 = request.POST.get('x200')
        x201 = request.POST.get('x201')
        x202 = request.POST.get('x202')
        x203 = request.POST.get('x203')
        x204 = request.POST.get('x204')
        x205 = request.POST.get('x205')
        x206 = request.POST.get('x206')
        x207 = request.POST.get('x207')
        x208 = request.POST.get('x208')
        x209 = request.POST.get('x209')
        x210 = request.POST.get('x210')
        x211 = request.POST.get('x211')
        x212 = request.POST.get('x212')
        x213 = request.POST.get('x213')
        x214 = request.POST.get('x214')
        x215 = request.POST.get('x215')
        x216 = request.POST.get('x216')
        x217 = request.POST.get('x217')
        x218 = request.POST.get('x218')
        x219 = request.POST.get('x219')
        x220 = request.POST.get('x220')
        x221 = request.POST.get('x221')
        x222 = request.POST.get('x222')
        x223 = request.POST.get('x223')
        x224 = request.POST.get('x224')
        x225 = request.POST.get('x225')
        x226 = request.POST.get('x226')
        x227 = request.POST.get('x227')
        x228 = request.POST.get('x228')
        x229 = request.POST.get('x229')
        x230 = request.POST.get('x230')
        x231 = request.POST.get('x231')
        x232 = request.POST.get('x232')
        x233 = request.POST.get('x233')
        x234 = request.POST.get('x234')
        x235 = request.POST.get('x235')
        x236 = request.POST.get('x236')
        x237 = request.POST.get('x237')
        x238 = request.POST.get('x238')
        x239 = request.POST.get('x239')
        x240 = request.POST.get('x240')
        x241 = request.POST.get('x241')
        x242 = request.POST.get('x242')
        x243 = request.POST.get('x243')
        x244 = request.POST.get('x244')
        x245 = request.POST.get('x245')
        x246 = request.POST.get('x246')
        x247 = request.POST.get('x247')
        x248 = request.POST.get('x248')
        x249 = request.POST.get('x249')
        x250 = request.POST.get('x250')
        x251 = request.POST.get('x251')
        x252 = request.POST.get('x252')
        x253 = request.POST.get('x253')
        x254 = request.POST.get('x254')
        x255 = request.POST.get('x255')
        x256 = request.POST.get('x256')
        x257 = request.POST.get('x257')
        x258 = request.POST.get('x258')
        x259 = request.POST.get('x259')
        x260 = request.POST.get('x260')
        x261 = request.POST.get('x261')
        x262 = request.POST.get('x262')
        x263 = request.POST.get('x263')
        x264 = request.POST.get('x264')
        x265 = request.POST.get('x265')
        x266 = request.POST.get('x266')
        x267 = request.POST.get('x267')
        x268 = request.POST.get('x268')
        x269 = request.POST.get('x269')
        x270 = request.POST.get('x270')
        x271 = request.POST.get('x271')
        x272 = request.POST.get('x272')
        x273 = request.POST.get('x273')
        x274 = request.POST.get('x274')
        x275 = request.POST.get('x275')
        x276 = request.POST.get('x276')
        x277 = request.POST.get('x277')
        x278 = request.POST.get('x278')
        x279 = request.POST.get('x279')
        x280 = request.POST.get('x280')
        x281 = request.POST.get('x281')
        x282 = request.POST.get('x282')
        x283 = request.POST.get('x283')
        x284 = request.POST.get('x284')
        x285 = request.POST.get('x285')
        x286 = request.POST.get('x286')
        x287 = request.POST.get('x287')
        x288 = request.POST.get('x288')
        x289 = request.POST.get('x289')
        x290 = request.POST.get('x290')
        x291 = request.POST.get('x291')
        x292 = request.POST.get('x292')
        x293 = request.POST.get('x293')
        x294 = request.POST.get('x294')
        x295 = request.POST.get('x295')
        x296 = request.POST.get('x296')
        x297 = request.POST.get('x297')
        x298 = request.POST.get('x298')
        x299 = request.POST.get('x299')
        x300 = request.POST.get('x300')
        x301 = request.POST.get('x301')
        x302 = request.POST.get('x302')
        x303 = request.POST.get('x303')
        x304 = request.POST.get('x304')
        x305 = request.POST.get('x305')
        x306 = request.POST.get('x306')
        x307 = request.POST.get('x307')
        x308 = request.POST.get('x308')
        x309 = request.POST.get('x309')
        x310 = request.POST.get('x310')
        x311 = request.POST.get('x311')
        x312 = request.POST.get('x312')
        x313 = request.POST.get('x313')
        x314 = request.POST.get('x314')
        x315 = request.POST.get('x315')
        x316 = request.POST.get('x316')
        x317 = request.POST.get('x317')
        x318 = request.POST.get('x318')
        x319 = request.POST.get('x319')
        x320 = request.POST.get('x320')
        x321 = request.POST.get('x321')
        x322 = request.POST.get('x322')
        x323 = request.POST.get('x323')
        x324 = request.POST.get('x324')
        x325 = request.POST.get('x325')
        x326 = request.POST.get('x326')
        x327 = request.POST.get('x327')
        x328 = request.POST.get('x328')
        x329 = request.POST.get('x329')
        x330 = request.POST.get('x330')
        x331 = request.POST.get('x331')
        x332 = request.POST.get('x332')
        x333 = request.POST.get('x333')
        x334 = request.POST.get('x334')
        x335 = request.POST.get('x335')
        x336 = request.POST.get('x336')
        x337 = request.POST.get('x337')
        x338 = request.POST.get('x338')
        x339 = request.POST.get('x339')
        x340 = request.POST.get('x340')
        x341 = request.POST.get('x341')
        x342 = request.POST.get('x342')
        x343 = request.POST.get('x343')
        x344 = request.POST.get('x344')
        x345 = request.POST.get('x345')
        x346 = request.POST.get('x346')
        x347 = request.POST.get('x347')
        x348 = request.POST.get('x348')
        x349 = request.POST.get('x349')
        x350 = request.POST.get('x350')
        x351 = request.POST.get('x351')
        x352 = request.POST.get('x352')
        x353 = request.POST.get('x353')
        x354 = request.POST.get('x354')
        x355 = request.POST.get('x355')
        x356 = request.POST.get('x356')
        x357 = request.POST.get('x357')
        x358 = request.POST.get('x358')
        x359 = request.POST.get('x359')
        x360 = request.POST.get('x360')
        x361 = request.POST.get('x361')
        x362 = request.POST.get('x362')
        x363 = request.POST.get('x363')
        x364 = request.POST.get('x364')
        x365 = request.POST.get('x365')
        x366 = request.POST.get('x366')
        x367 = request.POST.get('x367')
        x368 = request.POST.get('x368')
        x369 = request.POST.get('x369')
        x370 = request.POST.get('x370')
        x371 = request.POST.get('x371')
        x372 = request.POST.get('x372')
        x373 = request.POST.get('x373')
        x374 = request.POST.get('x374')
        x375 = request.POST.get('x375')
        x376 = request.POST.get('x376')
        x377 = request.POST.get('x377')
        x378 = request.POST.get('x378')
        x379 = request.POST.get('x379')
        x380 = request.POST.get('x380')
        x381 = request.POST.get('x381')
        x382 = request.POST.get('x382')
        x383 = request.POST.get('x383')
        x384 = request.POST.get('x384')
        x385 = request.POST.get('x385')
        x386 = request.POST.get('x386')
        x387 = request.POST.get('x387')
        x388 = request.POST.get('x388')
        x389 = request.POST.get('x389')
        x390 = request.POST.get('x390')
        x391 = request.POST.get('x391')
        x392 = request.POST.get('x392')
        x393 = request.POST.get('x393')
        x394 = request.POST.get('x394')
        x395 = request.POST.get('x395')
        x396 = request.POST.get('x396')
        x397 = request.POST.get('x397')
        x398 = request.POST.get('x398')
        x399 = request.POST.get('x399')
        x400 = request.POST.get('x400')
        x401 = request.POST.get('x401')
        x402 = request.POST.get('x402')
        x403 = request.POST.get('x403')
        x404 = request.POST.get('x404')
        x405 = request.POST.get('x405')
        x406 = request.POST.get('x406')
        x407 = request.POST.get('x407')
        x408 = request.POST.get('x408')
        x409 = request.POST.get('x409')
        x410 = request.POST.get('x410')
        x411 = request.POST.get('x411')
        x412 = request.POST.get('x412')
        x413 = request.POST.get('x413')
        x414 = request.POST.get('x414')
        x415 = request.POST.get('x415')
        x416 = request.POST.get('x416')
        x417 = request.POST.get('x417')
        x418 = request.POST.get('x418')
        x419 = request.POST.get('x419')
        x420 = request.POST.get('x420')
        x421 = request.POST.get('x421')
        x422 = request.POST.get('x422')
        x423 = request.POST.get('x423')
        x424 = request.POST.get('x424')
        x425 = request.POST.get('x425')
        x426 = request.POST.get('x426')
        x427 = request.POST.get('x427')
        x428 = request.POST.get('x428')
        x429 = request.POST.get('x429')
        x430 = request.POST.get('x430')
        x431 = request.POST.get('x431')
        x432 = request.POST.get('x432')
        x433 = request.POST.get('x433')
        x434 = request.POST.get('x434')
        x435 = request.POST.get('x435')
        x436 = request.POST.get('x436')
        x437 = request.POST.get('x437')
        x438 = request.POST.get('x438')
        x439 = request.POST.get('x439')
        x440 = request.POST.get('x440')
        x441 = request.POST.get('x441')
        x442 = request.POST.get('x442')
        x443 = request.POST.get('x443')
        x444 = request.POST.get('x444')
        x445 = request.POST.get('x445')
        x446 = request.POST.get('x446')
        x447 = request.POST.get('x447')
        x448 = request.POST.get('x448')
        x449 = request.POST.get('x449')
        x450 = request.POST.get('x450')
        x451 = request.POST.get('x451')
        x452 = request.POST.get('x452')
        x453 = request.POST.get('x453')
        x454 = request.POST.get('x454')
        x455 = request.POST.get('x455')
        x456 = request.POST.get('x456')
        x457 = request.POST.get('x457')
        x458 = request.POST.get('x458')
        x459 = request.POST.get('x459')
        x460 = request.POST.get('x460')
        x461 = request.POST.get('x461')
        x462 = request.POST.get('x462')
        x463 = request.POST.get('x463')
        x464 = request.POST.get('x464')
        x465 = request.POST.get('x465')
        x466 = request.POST.get('x466')
        x467 = request.POST.get('x467')
        x468 = request.POST.get('x468')
        x469 = request.POST.get('x469')
        x470 = request.POST.get('x470')
        x471 = request.POST.get('x471')
        x472 = request.POST.get('x472')
        x473 = request.POST.get('x473')
        x474 = request.POST.get('x474')
        x475 = request.POST.get('x475')
        x476 = request.POST.get('x476')
        x477 = request.POST.get('x477')
        x478 = request.POST.get('x478')
        x479 = request.POST.get('x479')
        x480 = request.POST.get('x480')
        x481 = request.POST.get('x481')
        x482 = request.POST.get('x482')
        x483 = request.POST.get('x483')
        x484 = request.POST.get('x484')
        x485 = request.POST.get('x485')
        x486 = request.POST.get('x486')
        x487 = request.POST.get('x487')
        x488 = request.POST.get('x488')
        x489 = request.POST.get('x489')
        x490 = request.POST.get('x490')
        x491 = request.POST.get('x491')
        x492 = request.POST.get('x492')
        x493 = request.POST.get('x493')
        x494 = request.POST.get('x494')
        x495 = request.POST.get('x495')
        x496 = request.POST.get('x496')
        x497 = request.POST.get('x497')
        x498 = request.POST.get('x498')
        x499 = request.POST.get('x499')
        x500 = request.POST.get('x500')
        x501 = request.POST.get('x501')
        x502 = request.POST.get('x502')
        x503 = request.POST.get('x503')
        x504 = request.POST.get('x504')
        x505 = request.POST.get('x505')
        x506 = request.POST.get('x506')
        x507 = request.POST.get('x507')
        x508 = request.POST.get('x508')
        x509 = request.POST.get('x509')
        x510 = request.POST.get('x510')
        x511 = request.POST.get('x511')
        x512 = request.POST.get('x512')
        x513 = request.POST.get('x513')
        x514 = request.POST.get('x514')
        x515 = request.POST.get('x515')
        x516 = request.POST.get('x516')
        x517 = request.POST.get('x517')
        x518 = request.POST.get('x518')
        x519 = request.POST.get('x519')
        x520 = request.POST.get('x520')
        x521 = request.POST.get('x521')
        x522 = request.POST.get('x522')
        x523 = request.POST.get('x523')
        x524 = request.POST.get('x524')
        x525 = request.POST.get('x525')
        x526 = request.POST.get('x526')
        x527 = request.POST.get('x527')
        x528 = request.POST.get('x528')
        x529 = request.POST.get('x529')
        x530 = request.POST.get('x530')
        x531 = request.POST.get('x531')
        x532 = request.POST.get('x532')
        x533 = request.POST.get('x533')
        x534 = request.POST.get('x534')
        x535 = request.POST.get('x535')
        x536 = request.POST.get('x536')
        x537 = request.POST.get('x537')
        x538 = request.POST.get('x538')
        x539 = request.POST.get('x539')
        x540 = request.POST.get('x540')
        x541 = request.POST.get('x541')
        x542 = request.POST.get('x542')
        x543 = request.POST.get('x543')
        x544 = request.POST.get('x544')
        x545 = request.POST.get('x545')
        x546 = request.POST.get('x546')
        x547 = request.POST.get('x547')
        x548 = request.POST.get('x548')
        x549 = request.POST.get('x549')
        x550 = request.POST.get('x550')
        x551 = request.POST.get('x551')
        x552 = request.POST.get('x552')
        x553 = request.POST.get('x553')
        x554 = request.POST.get('x554')
        x555 = request.POST.get('x555')
        x556 = request.POST.get('x556')
        x557 = request.POST.get('x557')
        x558 = request.POST.get('x558')
        x559 = request.POST.get('x559')
        x560 = request.POST.get('x560')
        x561 = request.POST.get('x561')
        x562 = request.POST.get('x562')
        x563 = request.POST.get('x563')
        x564 = request.POST.get('x564')
        x565 = request.POST.get('x565')
        x566 = request.POST.get('x566')
        x567 = request.POST.get('x567')
        x568 = request.POST.get('x568')
        x569 = request.POST.get('x569')
        x570 = request.POST.get('x570')
        x571 = request.POST.get('x571')
        x572 = request.POST.get('x572')
        x580 = request.POST.get('x580')
        x581 = request.POST.get('x581')
        male = f"""I was born on the {x1} in {x2}, a city in {x3} at {x4} hospital.
            My full name is {x5} .

            The people who decided on this name are {x6}.
            I was named this way because {x7}.Sometimes, I go by the nickname {x8} which I got from {x9}.
            I have a beautiful mother named {x10}. She was born on {x11} in {x12}.
            The place she grew up in {x13} was lovely just like her.
            Meanwhile, my father, {x14}, was born on the {x15}. He was raised in
            the city of {x16}.


            To complete my family, I have {x17} siblings.
            Their names are {x18}. They were born in {x19}. My mother gave birth
            to {20} on {x21}. On the other hand,
            {x22} was born on {x23}.
            I have a beautiful/handsome sister/brother who goes by the name {x24}. She/he was born on the
            {x25} in
            {x26}.
            My mother was raised well by her parents, {x7} and {x27}. My
            grandmother was named {x28}. Her birthday was on
            the {x29}; whereas, my grandpa, {x30}, was born on {x31} in the village of {x32}.


            On my father???s side, I was blessed with the lives of my grandma, {x33}, and my grandpa, {x34}.
            Granny was born on {x35} in {x36}. My grandfather???s birth date,
            however, was on {x37}. His family
            gleefully welcomed him on this day in the city of {x38}.



            I have the most gorgeous wife. She was named {x39} but I call her {x40}. I am thankful that she was successfully given
            birth to on the{x41} in the wonderful city of {x42}.

            {x43} and I were blessed with {x44} children who we named as {x45}.
            {x46} was born on {x47} in {x48}. On the
            other hand, {x49}???s birthdate is on {x50}. My wife gave
            birth to him/her in {x51}.



            Over the years, my children grew up and had their own kids, too. My adorable grandkids are named {x580} and {x581}.
            The first one is born in {x52} on the {x53}.
            {x54} was born on {x55} in the city of {x55}.



            I spend most of my free time {x56} while drinking {x57}.


            My most favorite sport is {x58} because I think it is {x59}


            My go-to vacation spot is {x61}. I find it {x62}.


            The meal that I enjoy the most is {x63}.


            My favorite song is called {x64}; it is sung by {x65}. The reason why
            I love it is that it reminds me of
            {x67}.


            Currently, my favorite television show is {x68}. Back then, I really loved the series {x69}.



            I have watched the movie {x70} several times already and I never get tired of it because it is
            {x71}.


            My hobbies are {x72}, {x73}, and {x74}. On
            the weekends, I also {x75} with my {x76}.



            The social gatherings that I usually enjoy are {x77}.


            My greatest talent is {x78}. I have used it in many ways throughout my life such as when I
            {x79}.


            The best characteristic that I love about myself is my {x80}.

            Sometimes, I wish I could stop being {x81}.



            Currently, I am living a {x81} life here in {x82} with my {x83}.
            On the weekdays, I spend most of my time {x84}. By the end of the day, I would feel {x85} and {x86}.



            I grew up in a {x87} neighborhood where I met various interesting people like {x88}.
            Remembering it, I can say that it was actually a {x89} place.


            My childhood home was {x90}. I enjoyed all of the {x91} mornings and
            {x92} nights in it. The house was
            suitable for a family of {x93} people. My time there was {x94}.



            My favorite place in this {x95} house was the {x96}. It had a special
            place in my heart because it {x97}.




            When I was younger, I had to do chores like {x98}.


            ({x99}) I got a daily/weekly/monthly allowance worth {x100}.



            The indoor activity that I enjoyed the most was {x101}. This was because {x102}.


            Back then, I really enjoyed {x103} outside the house.


            As a child, I was particularly skilled at {x104}.



            I also had some toys that cheered me up on sad days. These are {x105}.



            I had a special place that I called ???mine.??? It was this {x106} space filled with {x107}. I used to {x108} a lot when
            I stayed here.


            As a child, I always anticipated going out to {x109}.



            Being a boy, I {x110} not enjoy reading.
            (If yes) I liked collecting {x111} books!


            of this experience???{x112}
            I lived in a {x113} (Religious/Non-Religious) family.
            (If religious). I attended a church called {x114} which was located in {x115}. I remember the times when I {x116}.

            I {x117} baptized or dedicated as an infant.
            (If baptized) As an infant, I was baptized by {x118} in {x119}. My
            {x120} attended the celebration



            Some of the childhood experiences that helped me become who I am right now are {x121}.



            I remember having a childhood friend named {x122}. He/she was very {x123} and we had a {x124} time together.



            From my childhood, I will be eternally grateful for the {x125}. Because of it, I grew up to be
            a {x126} person.
            Family LIFE
            50 A family is a circle of love?????formed by memories,??filled with devotion.????



            My favorite memory with my dad was when {x127}. This is a special event for me because {x128}.



            My father???s insights on life and its adventures was {x129}. This made me become more {x130} regarding my own life.


            My father and I used to {x131} together and I really enjoyed it because {x132}.


            I think I have grown up to be like my father when it comes to my {x133}. I always think that I
            got this from him.


            One thing my dad always said was {x134}. I believe that this is actually a great {x135} and it helped me
            establish myself.


            My father worked as a/an {x136}. This job piqued / did not pique my interest because {x137}.


            One of the most memorable things about my mother from when I was a little boy was how she {x138}. This is because {x139}.

            My mom always had a {x140} outlook towards life. This attitude of hers affected me in a way
            that I became more {x141}.



            I am similar to her because she is {x142} just like me. My mother is the most {x143} woman I have ever met and I love her
            for it.


            Back when I was a child, I really liked {x144} with my mom. Until now, I still feel {x145} whenever I remember this.




            My mother???s occupation was {x146}. This helped me decide on my future career because I found it
            {x147} how she
            {x148}.


            My family was {x149}. We encountered problems such as {x150} and it
            was hard for me growing up. But
            I am now {x151} about my life. These circumstances have made me {x152}
            and {x153}.

            As I was growing up, my parents requested that I {x154}.


            This formed my mindset regarding parenting. In complete honesty, I actually require my children to {x155}, similar to /
            different from the obligations I had as a kid.


            Some of the qualities that my parents nurtured in me are my characteristics of being {x156} and
            {x157}. I am thankful for these.



            My parents always told me to be a {x158} person. Of course, I valued their encouragement
            because I loved them.



            I also loved my siblings/sister/brother so much. My fondest memories of them/him/her was that time when {x159}.

            Of course, being young means you get to enjoy the beauty of life without heavily thinking of the consequences. I played
            around with my
            siblings/brother/sister and we used to {x160}. It was funny for me back then but looking back,
            I think {x161}.
            My siblings/brother/sister and I were {x162}. We had {x163} days
            together.
            In addition to our lovely family, we had a pet {x164} / pets named {x165}. He/she/they were adorable!
            The thing I loved most about having {x166} growing up with me was {x167}. I loved {x168} with {x169}!
            On regular days, my family {x170} together. In the summer, we would often go {x171}. But most especially,
            we loved spending time together, either by {x172} or {x173}.
            My early memories of my grandparents was how they {x174}. My grandma would always {x175} while my grandpa {x176}.

            They lived in a lovely place in {x177}. Around their area, there were many {x178}. It was a {x179} neighborhood.
            My grandmother worked as a {x180} and my grandpa did some {x181} job.

            Whenever my family visited them / whenever they visited us, I remember that we always had an amazing time together. My
            grandma and
            grandpa prepares a delicious meal for us. Their {x182} was my favorite!

            I loved being with my grandparents because they were {x183}. I always watched them {x184} . They cared for me and my
            siblings/brother/sister.
            A valuable lesson that I learned from being with them was that {x185}. Aside from this, I was
            also inspired by them to be a {x186}
            person.
            The only things I remember about my great-grandparents are that they {x187}.
            I believe that my ancestors were {x188} and that I might have a/an {x189} origin.
            My favorite home-cooked meal was {x190} because it was honestly delicious and {x191}! It reminds me of {x192}.
            Whenever my family and I {x193} together, we would always prepare {x194}.
            We used to go out for dinner frequently/sometimes. When we do, I would always request that we go to {x195} or try other restaurants
            that serve {x196}.
            (Yes) Our house was a great place for celebrations. I remember having company often. My family???s friends or some of our
            other relatives
            would always come to visit or {x197} with us.
            (No) Although we were a happy family, we did not often have company perhaps because our place was {x198}.
            My family outings were {x199}! We would always go to {x200} and {x201} together. Holidays are my {x202} favorite season!
            In the winter, I remember {x203} with my siblings/brother/sister. As a whole family, we liked
            playing {x204}. My favorite
            winter food was {x205}. And drinks? Of course, {x206}.
            Family reunions are {x207} for me. I enjoyed {x208} whenever we held
            one.
            (No) I was not really close to my relatives.
            (Yes) I had close relationships with my other relatives especially with my {x209}. I am happy
            about these because I could always
            {x210} to them whenever I am {x211}.

            Every time I think about my family, the first thing that comes to mind was {x212}. I feel like
            I associated them with it because of
            the {x213} they bring to my life.

            Knowledge is the power??that gives us wings to soar.??

            I attended elementary at {x214} in {x215}. I often rode the {x216} to school and back OR I often biked/walked to
            school alone/with my {x217}.My earliest memories of going to {x218} was that I would always {x219}
            in {x220} Class. I also remember hanging out
            with my childhood friends named {x221} and {x222}.
            92 WHAT DID YOU ENJOY?? MOST ABOUT ELEMENTARY SCHOOL?????
            One thing I loved most about elementary was {x223} on {x224} days.
            But, I really hated that I had to {x225}.
            Next, I attended middle school at {x226}. Every day, I would go there via {x227}. Sometimes, I would {x228}.
            When I was in high school, I attended {x229}. It was a very {x230}
            school and I met a lot of {x231} people there.
            My favorite subjects in middle school were {x232} and {x233} because
            {x234}.
            Meanwhile, in high school, I really liked going to {x235} class. The teacher was really {x236} and my classmates were
            {x237}.
            Some extracurricular activities that I enjoyed the most were {x238}. I chose these because
            {x239}.
            Over the years, I have received some special awards such as {x240}.
            I had a favorite teacher whose name was {x241}. I can say that she/he had a big influence on
            shaping who I am now by {x242}.
            Back when I was still in school, there were many fashion trends that arose such as {x243}.
            (Yes) I participated in them because {x244}.
            (No) I did not participate much when it comes to these because {x245}.
            The most popular songs that I remember around the time I was studying were {x246}. I really
            {x247} this kind of music.
            Meanwhile, the highest grossing movies were {x248}. People {x249}
            these so much!
            The television shows that were much awaited were {x250}.
            Lastly, celebrities such as {x251} were having their primes then.
            The parties that I attended were mostly {x252}. Some of the party-goers were from {x253}. I can still remember
            how {x254} the crowd was.
            (No) I didn???t have a car when I was in high school but if I did it probably would be a __________.
            (Yes) I had a car when I was a teenager and it was a {x255}. I was {x256} about how it looks like.
            I really went places with that car.
            My middle school and high school years were a bit difficult because of {x257}. But, as a whole
            I think I really {x258}
            my teenage years.
            DURING YOUR MIDDLE SCHOOL AND HIGH SCHOOL YEARS???
            I am happy that I got to {x259} while I was schooling. It was a great privilege for me.
            change with time?????
            During this time, I was thinking about my goal of becoming a {x260} and I really hoped to
            achieve my dreams such as
            that of {x261}. Over time, I continued/stopped inching towards these goals.
            After graduation, I chose to follow the path of becoming a {x262}.
            I went to college / a career training school called {x263} in the city of {x264}. I took up a degree in the field of
            {x265}.
            I had to move away from home to continue studying and it was {x266}. I was looking forward to
            {x267} but I really felt
            {x268} when I was away from my family.
            I lived in an apartment/dorm nearby. It was {x269}, {x270}, and {x271}. I had a {x272} time studying when I was
            there.
            (with roommate) I had a roommate whose name was {x273}. He/she was a {x274} person.
            My most favorite college memories were the one at {x275} with my {x276}. Those experiences were {x277}
            and unforgettable.
            On??the Job??

            Any job can be made great.??It???s the worker???not the work?????that counts

            When I was young, I tried to gain money by {x278}. My earnings were used to pay for my {x279}.


            My first career-oriented job after graduation was a {x280} at {x281}.
            Here, I would be the one responsible for
            {x282}.
            When I found out that I got accepted in this job, I was very {x283}. I thought that this can
            help me in {x284}.
            The one thing I love most about my first job was {x285}. The environment in the workplace was
            also {x286}.
            Among the jobs that I tried and had in the past, the one in which I probably had the most fun was when I was working at
            {x287}
            as a {x288}. This is due to the fact that {x289}.

            Meanwhile, the worst job was in {x290}. I mostly did not enjoy working here because of {x291}.
            The most rewarding out of all, however, was the job at {x292}. This is because I was {x293}. I really love
            {x294} about this job.
            Of course, some opportunities can only be achieved when you move out of your comfort zone. As for me, I had to move away
            when I
            was working at {x295} in {x296}. I felt {x297} because of it but I am {x298} that I took it.
            For some jobs, I had to go places for {x299} events. The most memorable place I visited while
            doing so was a {x300} in {x301}.
            I had a coworker / superior who displayed the role of a friendly and trustworthy mentor to me. His/her name was {x302} and
            he/she taught me how to {x303}.
            (If yes) Over the years, I was able to be a mentor to others, too. I believe it was a {x304}
            experience for me.
            (If no) I might not have been an official mentor to others myself, but I believe that I was also able to help my
            colleagues in various ways.

            At work, I met all types of people but I found {x305} friends, too.
            When I???m just at home, I like to work on {x306}.
            But, I usually avoid doing {x307} because {x308}.
            Love??AND??Marriage????
            130 When love touches our hearts,??happiness fills our days.??

            I remember having a crush on {x309} when I was younger. I believe she was the first person I
            truly admired.
            The first boy party that I attended was when I was {x310} years old. It was held at {x311}..
            My first kiss was {x312}. I remember how I felt really {x313}
            afterwards.
            My first ever date was {x314}. It went {x315}. I had a {x316} time with {x317}.
            When that happened, lovers usually {x318} when they went out together and hung out. The kind of
            date nights was very {x319}
            compared to now.
            I met my lovely wife when I was {x320} years old.


            I will be eternally grateful that our paths crossed on {x321} in {x322}. If it weren???t for the {x323},
            I wouldn???t have seen her.
            She was {x324}, {x325}, and {x326}. Those
            qualities really captured my attention.
            Initially, I thought that she was {x327}. Over time, I realized how {x328} my first impression was compared to how
            she really is.
            I courted her for {x329} months. She was definitely worth the wait.
            When we just started dating, we really loved {x330} together. Some other things that we enjoyed
            doing were {x331}
            and {x332}.
            I knew she was the one when {x333} after I realized that she could be {x334}.
            The marriage proposal was {x335} and I am sincerely {x336} about it!
            There were {x337} everywhere while I
            was waiting for her response.
            We officially tied the knot on {x338} at a {x339} in {x340}.


            I wore a {x341}.

            While she wore a beautiful and {x342} wedding dress/gown.??

            It was a small/big wedding. We had about {x343} guests.

            For our first dance as husband and wife, we swayed to the song entitled {x344} which was chosen
            because {x345}.
            The most remarkable memory of mine from that special day was {x346}.

            Recall a special moment or event from the honeymoon.??
            Our honeymoon was {x347}! We went to {x348} wherein we {x349}. What I loved most about this
            experience was the fact that {x350}.


            After getting married, we lived in {x351}. I clearly remember how {x352} our home was.


            Early into our marriage, we had {x353} nights where we would enjoy dinner together over a
            {x354}.
            We started thinking about having children when {x355}. I really looked forward to {x356} and seeing my wife
            {x357} for our kids.


            WHEN YOU WERE FIRST MARRIED???What were some of the fun things you did with them???
            As a couple, we had some close friends. The ones that we mostly hung out with were named {x358}.
            We would always {x359} together and it felt {x360}! I {x361} spending time with them.


            {x362} and I really loved {x363} whenever we had free time. Aside from
            this, we also enjoyed {x364}.
            For me, marriage has been rewarding because {x365}.
            To be able to withstand any hardship, I believe that the most important key to a healthy marriage is {x366}.
            Of course in our marriage we also had hard times wherein we needed to be there for each other more. These instances that
            required
            sharing and companionship happened when {x367}.
            My daily relationship with my loving wife has been {x368}. Right now, my favorite thing about
            being married to is {x369}.
            Parenting????
            To be a father is to protect,??nurture, and guide,??but most of all, to love.????


            When I found out that I was going to be a dad, I felt {x370}. I remember that day being a
            {x371}
            one.
            I lived in {x372}
            My FIRST CHILD WAS BORN on ??{x373}
            My growing family then lived at a {x374} in {x375}.


            Back then, our situation was {x376}.
            We had problems such as {x377} OR We did not have any problems.


            Every time I looked at my firstborn when he/she was an infant, I felt {x378}. Every day with
            him/her was really
            {x379}.


            Becoming a father was {x380}. It caused me to have a more {x381}
            outlook on life. I realized that {x382}.
            168 WHAT IS YOUR MOST VIVID MEMORY??OF YOUR CHILDREN???S EARLY YEARS?????
            I have some crystal clear memories of my children when they were still young. These include the time when {x383} and
            also that instance when {x384}.


            Back then, I really enjoyed {x386} with them. When they grew up a bit, we would always {x385}.
            Of course, there had to be some days that I would need to spend alone with my wife. Whenever we took the days off for
            our special dates,
            we would {x387}.

            As a parent, I believe that it is undeniable that I have similarities with my kids. These include {x388}.
            As for them, my kids are similar in a way that they are all {x389}. This might be because
            {x390}.
            My spouse and I tried to instill the qualities of being {x391}, {x392}, and {x393} to our kids.
            I know that I have been blessed to be a father because I get to experience {x394}. This is what
            I consider my greatest joy
            in this {x395} role.
            Because life is not perfect, our family had problems, too. The greatest challenge that I experienced as a dad to {x396} beautiful kids
            was {x397}.
            I was raised in a {x398} family which is similar/different to my children???s upbringing. They
            grew up in a {x399} house, a
            {x400} neighborhood, with {x401} parents.
            THAT YOU WISH YOU???D KNOWN WHEN YOU??FIRST BECAME A FATHER?????
            Sometimes, I wish that I knew better when I became a father to my firstborn. One thing that I learned through time that
            I could
            have known back when I was raising {x402} was {x403}.
            I am a {x404} person. Somehow I wish my kids can grow up to be {x405}
            -- opposite/similar to me.
            Being a father taught me a lot of {x406} lessons but to me the most important thing among all
            these is {x407}.
            This is due to the fact that {x408}.


            Life offers so many??wonderful things to share,??so many special joys to celebrate.????

            We would always {x409} on my birthday when I was young. The guests were usually {x410}. It was a {x411}
            celebration.


            My favorite memory of a birthday party was when {x412}. This happened on my {x413} th birthday.
            The most special presents that I ever received are {x414}. For me, they were wonderful because
            {x415}.
            I often requested that my parents cook/make/buy {x416} to serve on my birthdays. I really loved
            these food because
            {x417}.
            Apart from the celebration of my birth, I had other unique parties held at our humble abode. These include {x418}.
            The ambiance of the surroundings during this feast was {x419}. Guests had to wear {x420}.
            As a child, my favorite religious festivity is {x421}. We would {x422}
            together as a family and {x423}.
            We prepare meals such as {x424} to feast on.
            Among these types of celebrations, the main thing that stands out in my memory is {x425} due to
            the fact that
            {x426}.

            I really liked the {x427} that we buy/make during my childhood. It tasted {x428} and {x429}.
            My favorite christmas carol was {x420}. Right now, {x431} is my
            favorite.
            where??it??came??from?????
            What my family told us about Santa Claus was that he was/wasn???t real. I always knew/didn???t know where the gifts from my
            Christmas
            stocking / ornament came from.
            During these holidays, we often gave presents to each other. My most loved gift was the {x432}
            from my {x433}
            because {x434}.
            Meanwhile, the most memorable present that I gave someone was a {x435}. This was for my {x436}.
            I still remember how he/she {x437} it.
            Growing up, I always loved the religious tradition we had in our family. Now that I have my own, I continued to {x438}.
            As a parent, the most meaningful Christmas for me was when {x439} because {x440}.
            195 HOW DID YOU CELEBRATE THANKSGIVING???Did you have a favourite Thanksgiving tradition?????
            For Thanksgiving, my family usually {x441}. The tradition that I love most is {x442}.
            Preparing and eating Thanksgiving food is also {x443}.
            When I was a kid, I really {x444} Australia day. The neighborhood would always be {x445} and there were {x446}
            everywhere!
            What was your favourite Halloween treat?????
            I did/didn???t really enjoy halloween. I remember an especially fun costume worn by {x447}. It
            was a {x448}.
            I also {x449} to trick-or-treat! My favorite treat was {x450} since
            {x451}. One memory that I have of a really enjoyable holiday celebration was when {x452}. It happened around the time that {x453}. I think it was a meaningful experience for me because {x454}.
            Moment by moment,??day by day,??families create a lifetime of memories.??The happiest time of my life, I must say, is when {x455}. I cannot explain the joy that I felt because {x456}. To me, it???s an experience that cannot be beaten by anything else. Meanwhile, the saddest for me was when {x457}. I believe I had a {x458} time moving on from this
            because {x459}. Over the years, I had many commitments and responsibilities but there was a time wherein I was always occupied.
            The busiest I have ever been was when {x460}. It was due to the fact that {x461}. On the other hand, I had relaxing days, too, but I am confident to say that I was most comfortable and at ease when
            {x462}. A life-changing event that really influenced me in many ways was when {x463}. Somehow, it
            helped me {x464}. One political event that I participated in or witnessed over the years was {x465}. It made a
            really strong impression on for the reason that {x466}.  (I have) I served in the military back then. It was a {x467} experience, while at the same
            time, there were instances that {x468} me such as {x469}. (Other family members have) Some of my relatives had to serve in the military. I was really {x470} about it and it
            often {x471} me thinking about what was happening to them while in there.
            I can proudly say that I was able to {x472}. This had been fulfilling for me because {x473}.
            I have been in an accident/major surgery/long illness. This involved me being {x474}.
            It sincerely didn???t have / had a lasting effect on me because it made me {x475}.
            My family experienced a tragic time when {x476} happened. I have always been a {x477} person and although I was
            {x478}, I made sure that I would still be able to {x479}.
            YOU HAD TO MAKE IN YOUR LIFE???HAD TO MAKE IN YOUR LIFE???Would you make the same choice again?????
            The most difficult choice that I made was {x480}. I do not regret / regret it until now and if
            I would be given a chance to choose a different option, I would {x481}. Throughout the years, I really didn???t travel much / went to a lot of places but the most memorable experience I had
            while traveling was when I went to {x482} alone / with {x483}. There, I / we did
            activities such as {x484}. The first time I rode an airplane was when I was off to {x485} when I was {x486} years old. I had to go there because of
            {x487}. (No) I did not get the chance to travel abroad but I bet I would love to see {x488}.
            (Yes) I had the opportunity of traveling abroad and it was {x489}! I enjoyed {x490} because {x491}.
            Among all the tourist spots and vacation places that I have been to, I can say that the most interesting and exciting
            was when I went
            to {x492}. It was special because {x493}.
            I {x494} helping people because I believe that {x495}. One person that
            I extended my helping hands to was named {x496}.
            He/she needed assistance in {x497} so I {x498}.
            I also dedicated myself to a cause / organization for the {x499}. I participated in it with an
            open heart because {x500}.
            How did you benefit from it???
            I was also given the chance to join competitive activities like {x501} which helped me grow in
            a way that {x502}.
            Being on earth for {x503} years is a lot of work and over the years I did many {x504} things. Thankfully, my efforts were
            professionally recognized when I {x505}. Upon receiving my award, I felt {x506}.
            The most important invention in my lifetime was {x507}. I will be eternally grateful that it
            existed because
            {x508}.
            Some of the most remarkable political / international events that I witnessed or participated in while I am living were
            {x509}.
            These were memorable because {x510}.
            Science has always {x511} me but, in particular, {x512} piqued my
            interest.
            Growing up to be who I am today and comparing my upbringing to the youth of the current times, I can say that we are
            very
            similar / different in ways such as {x513}. This might be due to the fact that {x514} nowadays
            compared to back then.
            Even though I was {x515}, I don???t think I would want to change that about how I lived my life
            even if I would be given a chance to do
            so.
            Although, I guess I would have changed {x516} because {x517}.
            In the next ten years, I wish my family will become {x518} so that {x519}.
            For the world to be a better and happier place however, I hope that {x520} will change and
            {x521}
            can be more {x522}.
            Inspiration????How great it is??to have the freedom to dream??and the opportunity??to make those dreams come true.??

            The people I would like to thank for helping me be the person I am today are {x523}. They
            helped me
            {x524}.
            Whenever I needed help, I would always approach {x525} and he/she always had the answers that
            could make me {x526}.
            (No) Religion did not really play a significant role in my life.
            (Yes) Religion helped me be a {x527} person. I relied on my faith every time I {x528}.
            A poem/passage/quote that I learned to live by or admired sincerely was {x529} by {x530}. This is due to the fact that
            {x531}.
            If worst comes to worst and I am only allowed to keep a single family photo, it would be that of {x532}. This is {x533}
            for me because it reminds me of {x534}.
            Perhaps, the greatest possession that I have is my {x535}. It is unbeatable by any other
            because {x536}.
            The greatest gifts in my life are {x537}. I will forever be grateful for these.
            (No) I never felt that I was born to become someone.
            (Yes) I have always felt that I was born to be {x538} -- that I was called to {x539}.
            Back when I was little, I looked up to {x540} the most because {x541}.
            Somehow, I grew up to be
            closely similar to/different from them.
            A celebrity that I admired was {x542} because of his/her {x543}.
            If not, who would you like to hear and why?????
            (No) I have never been able to listen to a public speaker but if I would be given the chance, I want to hear {x544} because he/she
            {x545}.
            (Yes) I was able to witness {x546} speaking live and it greatly impacted me in a way that
            {x547}.

            What are some of the insights that you???ve received?????
            One book that has always made a big impression on me was {x548} by {x549}. I loved this author???s works because
            they taught me that {x550}.
            When I was young, I was told by {x551} that I should {x552}. They
            taught me this lesson
            when I was {x553}.
            To be able to work well with other people, one should be {x554}. It requires {x555} to build a lasting relationship.
            Success is something that {x556}. It does not {x557} and it is not
            {x558}.
            The secret to it would be {x559}. That is what I realized in my life on earth.
            CHARACTERISTICS OF A GOOD FRIEND?????
            One can only be considered a good friend if they are {x560}, {x561},
            and {x562}. If not, then there must be
            {x563}.
            What I value most about my family is the fact that {x564}. Even though there are hardships,
            we {x565} together.


            My life on earth has been emotionally {x566}, physically {x567}, and
            wholly {x568}. People have come
            and gone, seasons have changed countless times, and days have been numbered one by one. The single most important lesson
            I???ve learned in this {x569} world is that {x570}.
            The greatest advice I can give right now is that {x571}. I am hoping that people will listen and that my family will deem this as unforgettable and {x572}.
            PLEASE RECORD ANY OTHER INFORMATION YOU WISH TO SHARE """

        obj = Stroy(owner=request.user,
                    story_name='First Story', the_story=male)
        obj.save()
    return render(request, 'story/mother.html')


def grand_parent_story(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        x5 = request.POST.get('x5')
        x6 = request.POST.get('x6')
        x7 = request.POST.get('x7')
        x8 = request.POST.get('x8')
        x9 = request.POST.get('x9')
        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')
        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')
        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')
        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')
        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')
        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')
        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')
        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')
        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')
        x100 = request.POST.get('x100')
        x101 = request.POST.get('x101')
        x102 = request.POST.get('x102')
        x103 = request.POST.get('x103')
        x104 = request.POST.get('x104')
        x105 = request.POST.get('x105')
        x106 = request.POST.get('x106')
        x107 = request.POST.get('x107')
        x108 = request.POST.get('x108')
        x109 = request.POST.get('x109')
        x110 = request.POST.get('x110')
        x111 = request.POST.get('x111')
        x112 = request.POST.get('x112')
        x113 = request.POST.get('x113')
        x114 = request.POST.get('x114')
        x115 = request.POST.get('x115')
        x116 = request.POST.get('x116')
        x117 = request.POST.get('x117')
        x118 = request.POST.get('x118')
        x119 = request.POST.get('x119')
        x120 = request.POST.get('x120')
        x121 = request.POST.get('x121')
        x122 = request.POST.get('x122')
        x123 = request.POST.get('x123')
        x124 = request.POST.get('x124')
        x125 = request.POST.get('x125')
        x126 = request.POST.get('x126')
        x127 = request.POST.get('x127')
        x128 = request.POST.get('x128')
        x129 = request.POST.get('x129')
        x130 = request.POST.get('x130')
        x131 = request.POST.get('x131')
        x132 = request.POST.get('x132')
        x133 = request.POST.get('x133')
        x134 = request.POST.get('x134')
        x135 = request.POST.get('x135')
        x136 = request.POST.get('x136')
        x137 = request.POST.get('x137')
        x138 = request.POST.get('x138')
        x139 = request.POST.get('x139')
        x140 = request.POST.get('x140')
        x141 = request.POST.get('x141')
        x142 = request.POST.get('x142')
        x143 = request.POST.get('x143')
        x144 = request.POST.get('x144')
        x145 = request.POST.get('x145')
        x146 = request.POST.get('x146')
        x147 = request.POST.get('x147')
        x148 = request.POST.get('x148')
        x149 = request.POST.get('x149')
        x150 = request.POST.get('x150')
        x151 = request.POST.get('x151')
        x152 = request.POST.get('x152')
        x153 = request.POST.get('x153')
        x154 = request.POST.get('x154')
        x155 = request.POST.get('x155')
        x156 = request.POST.get('x156')
        x157 = request.POST.get('x157')
        x158 = request.POST.get('x158')
        x159 = request.POST.get('x159')
        x160 = request.POST.get('x160')
        x161 = request.POST.get('x161')
        x162 = request.POST.get('x162')
        x163 = request.POST.get('x163')
        x164 = request.POST.get('x164')
        x165 = request.POST.get('x165')
        x166 = request.POST.get('x166')
        x167 = request.POST.get('x167')
        x168 = request.POST.get('x168')
        x169 = request.POST.get('x169')
        x170 = request.POST.get('x170')
        x171 = request.POST.get('x171')
        x172 = request.POST.get('x172')
        x173 = request.POST.get('x173')
        x174 = request.POST.get('x174')
        x175 = request.POST.get('x175')
        x176 = request.POST.get('x176')
        x177 = request.POST.get('x177')
        x178 = request.POST.get('x178')
        x179 = request.POST.get('x179')
        x180 = request.POST.get('x180')
        x181 = request.POST.get('x181')
        x182 = request.POST.get('x182')
        x183 = request.POST.get('x183')
        x184 = request.POST.get('x184')
        x185 = request.POST.get('x185')
        x186 = request.POST.get('x186')
        x187 = request.POST.get('x187')
        x188 = request.POST.get('x188')
        x189 = request.POST.get('x189')
        x190 = request.POST.get('x190')
        x191 = request.POST.get('x191')
        x192 = request.POST.get('x192')
        x193 = request.POST.get('x193')
        x194 = request.POST.get('x194')
        x195 = request.POST.get('x195')
        x196 = request.POST.get('x196')
        x197 = request.POST.get('x197')
        x198 = request.POST.get('x198')
        x199 = request.POST.get('x199')
        x200 = request.POST.get('x200')
        x201 = request.POST.get('x201')
        x202 = request.POST.get('x202')
        x203 = request.POST.get('x203')
        x204 = request.POST.get('x204')
        x205 = request.POST.get('x205')
        x206 = request.POST.get('x206')
        x207 = request.POST.get('x207')
        x208 = request.POST.get('x208')
        x209 = request.POST.get('x209')
        x210 = request.POST.get('x210')
        x211 = request.POST.get('x211')
        x212 = request.POST.get('x212')
        x213 = request.POST.get('x213')
        x214 = request.POST.get('x214')
        x215 = request.POST.get('x215')
        x216 = request.POST.get('x216')
        x217 = request.POST.get('x217')
        x218 = request.POST.get('x218')
        x219 = request.POST.get('x219')
        x220 = request.POST.get('x220')
        x221 = request.POST.get('x221')
        x222 = request.POST.get('x222')
        x223 = request.POST.get('x223')
        x224 = request.POST.get('x224')
        x225 = request.POST.get('x225')
        x226 = request.POST.get('x226')
        x227 = request.POST.get('x227')
        x228 = request.POST.get('x228')
        x229 = request.POST.get('x229')
        x230 = request.POST.get('x230')
        x231 = request.POST.get('x231')
        x232 = request.POST.get('x232')
        x233 = request.POST.get('x233')
        x234 = request.POST.get('x234')
        x235 = request.POST.get('x235')
        x236 = request.POST.get('x236')
        x237 = request.POST.get('x237')
        x238 = request.POST.get('x238')
        x239 = request.POST.get('x239')
        x240 = request.POST.get('x240')
        x241 = request.POST.get('x241')
        x242 = request.POST.get('x242')
        x243 = request.POST.get('x243')
        x244 = request.POST.get('x244')
        x245 = request.POST.get('x245')
        x246 = request.POST.get('x246')
        x247 = request.POST.get('x247')
        x248 = request.POST.get('x248')
        x249 = request.POST.get('x249')
        x250 = request.POST.get('x250')
        x251 = request.POST.get('x251')
        x252 = request.POST.get('x252')
        x253 = request.POST.get('x253')
        x254 = request.POST.get('x254')
        x255 = request.POST.get('x255')
        x256 = request.POST.get('x256')
        x257 = request.POST.get('x257')
        x258 = request.POST.get('x258')
        x259 = request.POST.get('x259')
        x260 = request.POST.get('x260')
        x261 = request.POST.get('x261')
        x262 = request.POST.get('x262')
        x263 = request.POST.get('x263')
        x264 = request.POST.get('x264')
        x265 = request.POST.get('x265')
        x266 = request.POST.get('x266')
        x267 = request.POST.get('x267')
        x268 = request.POST.get('x268')
        x269 = request.POST.get('x269')
        x270 = request.POST.get('x270')
        x271 = request.POST.get('x271')
        x272 = request.POST.get('x272')
        x273 = request.POST.get('x273')
        x274 = request.POST.get('x274')
        x275 = request.POST.get('x275')
        x276 = request.POST.get('x276')
        x277 = request.POST.get('x277')
        x278 = request.POST.get('x278')
        x279 = request.POST.get('x279')
        x280 = request.POST.get('x280')
        x281 = request.POST.get('x281')
        x282 = request.POST.get('x282')
        x283 = request.POST.get('x283')
        x284 = request.POST.get('x284')
        x285 = request.POST.get('x285')
        x286 = request.POST.get('x286')
        x287 = request.POST.get('x287')
        x288 = request.POST.get('x288')
        x289 = request.POST.get('x289')
        x290 = request.POST.get('x290')
        x291 = request.POST.get('x291')
        x292 = request.POST.get('x292')
        x293 = request.POST.get('x293')
        x294 = request.POST.get('x294')
        x295 = request.POST.get('x295')
        x296 = request.POST.get('x296')
        x297 = request.POST.get('x297')
        x298 = request.POST.get('x298')
        x299 = request.POST.get('x299')
        x300 = request.POST.get('x300')
        x301 = request.POST.get('x301')
        x302 = request.POST.get('x302')
        x303 = request.POST.get('x303')
        x304 = request.POST.get('x304')
        x305 = request.POST.get('x305')
        x306 = request.POST.get('x306')
        x307 = request.POST.get('x307')
        x308 = request.POST.get('x308')
        x309 = request.POST.get('x309')
        x310 = request.POST.get('x310')
        x311 = request.POST.get('x311')
        x312 = request.POST.get('x312')
        x313 = request.POST.get('x313')
        x314 = request.POST.get('x314')
        x315 = request.POST.get('x315')
        x316 = request.POST.get('x316')
        x317 = request.POST.get('x317')
        x318 = request.POST.get('x318')
        x319 = request.POST.get('x319')
        x320 = request.POST.get('x320')
        x321 = request.POST.get('x321')
        x322 = request.POST.get('x322')
        x323 = request.POST.get('x323')
        x324 = request.POST.get('x324')
        x325 = request.POST.get('x325')
        x326 = request.POST.get('x326')
        x327 = request.POST.get('x327')
        x328 = request.POST.get('x328')
        x329 = request.POST.get('x329')
        x330 = request.POST.get('x330')
        x331 = request.POST.get('x331')
        x332 = request.POST.get('x332')
        x333 = request.POST.get('x333')
        x334 = request.POST.get('x334')
        x335 = request.POST.get('x335')
        x336 = request.POST.get('x336')
        x337 = request.POST.get('x337')
        x338 = request.POST.get('x338')
        x339 = request.POST.get('x339')
        x340 = request.POST.get('x340')
        x341 = request.POST.get('x341')
        x342 = request.POST.get('x342')
        x343 = request.POST.get('x343')
        x344 = request.POST.get('x344')
        x345 = request.POST.get('x345')
        x346 = request.POST.get('x346')
        x347 = request.POST.get('x347')
        x348 = request.POST.get('x348')
        x349 = request.POST.get('x349')
        x350 = request.POST.get('x350')
        x351 = request.POST.get('x351')
        x352 = request.POST.get('x352')
        x353 = request.POST.get('x353')
        x354 = request.POST.get('x354')
        x355 = request.POST.get('x355')
        x356 = request.POST.get('x356')
        x357 = request.POST.get('x357')
        x358 = request.POST.get('x358')
        x359 = request.POST.get('x359')
        x360 = request.POST.get('x360')
        x361 = request.POST.get('x361')
        x362 = request.POST.get('x362')
        x363 = request.POST.get('x363')
        x364 = request.POST.get('x364')
        x365 = request.POST.get('x365')
        x366 = request.POST.get('x366')
        x367 = request.POST.get('x367')
        x368 = request.POST.get('x368')
        x369 = request.POST.get('x369')
        x370 = request.POST.get('x370')
        x371 = request.POST.get('x371')
        x372 = request.POST.get('x372')
        x373 = request.POST.get('x373')
        x374 = request.POST.get('x374')
        x375 = request.POST.get('x375')
        x376 = request.POST.get('x376')
        x377 = request.POST.get('x377')
        x378 = request.POST.get('x378')
        x379 = request.POST.get('x379')
        x380 = request.POST.get('x380')
        x381 = request.POST.get('x381')
        x382 = request.POST.get('x382')
        x383 = request.POST.get('x383')
        x384 = request.POST.get('x384')
        x385 = request.POST.get('x385')
        x386 = request.POST.get('x386')
        x387 = request.POST.get('x387')
        x388 = request.POST.get('x388')
        x389 = request.POST.get('x389')
        x390 = request.POST.get('x390')
        x391 = request.POST.get('x391')
        x392 = request.POST.get('x392')
        x393 = request.POST.get('x393')
        x394 = request.POST.get('x394')
        x395 = request.POST.get('x395')
        x396 = request.POST.get('x396')
        x397 = request.POST.get('x397')
        x398 = request.POST.get('x398')
        x399 = request.POST.get('x399')
        x400 = request.POST.get('x400')
        x401 = request.POST.get('x401')
        x402 = request.POST.get('x402')
        x403 = request.POST.get('x403')
        x404 = request.POST.get('x404')
        x405 = request.POST.get('x405')
        x406 = request.POST.get('x406')
        x407 = request.POST.get('x407')
        x408 = request.POST.get('x408')
        x409 = request.POST.get('x409')
        x410 = request.POST.get('x410')
        x411 = request.POST.get('x411')
        x412 = request.POST.get('x412')
        x413 = request.POST.get('x413')
        x414 = request.POST.get('x414')
        x415 = request.POST.get('x415')
        x416 = request.POST.get('x416')
        x417 = request.POST.get('x417')
        x418 = request.POST.get('x418')
        x419 = request.POST.get('x419')
        x420 = request.POST.get('x420')
        x421 = request.POST.get('x421')
        x422 = request.POST.get('x422')
        x423 = request.POST.get('x423')
        x424 = request.POST.get('x424')
        x425 = request.POST.get('x425')
        x426 = request.POST.get('x426')
        x427 = request.POST.get('x427')
        x428 = request.POST.get('x428')
        x429 = request.POST.get('x429')
        x430 = request.POST.get('x430')
        x431 = request.POST.get('x431')
        x432 = request.POST.get('x432')
        x433 = request.POST.get('x433')
        x434 = request.POST.get('x434')
        x435 = request.POST.get('x435')
        x436 = request.POST.get('x436')
        x437 = request.POST.get('x437')
        x438 = request.POST.get('x438')
        x439 = request.POST.get('x439')
        x440 = request.POST.get('x440')
        x441 = request.POST.get('x441')
        x442 = request.POST.get('x442')
        x443 = request.POST.get('x443')
        x444 = request.POST.get('x444')
        x445 = request.POST.get('x445')
        x446 = request.POST.get('x446')
        x447 = request.POST.get('x447')
        x448 = request.POST.get('x448')
        x449 = request.POST.get('x449')
        x450 = request.POST.get('x450')
        x451 = request.POST.get('x451')
        x452 = request.POST.get('x452')
        x453 = request.POST.get('x453')
        x454 = request.POST.get('x454')
        x455 = request.POST.get('x455')
        x456 = request.POST.get('x456')
        x457 = request.POST.get('x457')
        x458 = request.POST.get('x458')
        x459 = request.POST.get('x459')
        x460 = request.POST.get('x460')
        x461 = request.POST.get('x461')
        x462 = request.POST.get('x462')
        x463 = request.POST.get('x463')
        x464 = request.POST.get('x464')
        x465 = request.POST.get('x465')
        x466 = request.POST.get('x466')
        x467 = request.POST.get('x467')
        x468 = request.POST.get('x468')
        x469 = request.POST.get('x469')
        x470 = request.POST.get('x470')
        x471 = request.POST.get('x471')
        x472 = request.POST.get('x472')
        x473 = request.POST.get('x473')
        x474 = request.POST.get('x474')
        x475 = request.POST.get('x475')
        x476 = request.POST.get('x476')
        x477 = request.POST.get('x477')
        x478 = request.POST.get('x478')
        x479 = request.POST.get('x479')
        x480 = request.POST.get('x480')
        x481 = request.POST.get('x481')
        x482 = request.POST.get('x482')
        x483 = request.POST.get('x483')
        x484 = request.POST.get('x484')
        x485 = request.POST.get('x485')
        x486 = request.POST.get('x486')
        x487 = request.POST.get('x487')
        x488 = request.POST.get('x488')
        x489 = request.POST.get('x489')
        x490 = request.POST.get('x490')
        x491 = request.POST.get('x491')
        x492 = request.POST.get('x492')
        x493 = request.POST.get('x493')
        x494 = request.POST.get('x494')
        x495 = request.POST.get('x495')
        x496 = request.POST.get('x496')
        x497 = request.POST.get('x497')
        x498 = request.POST.get('x498')
        x499 = request.POST.get('x499')
        x500 = request.POST.get('x500')
        x501 = request.POST.get('x501')
        x502 = request.POST.get('x502')
        x503 = request.POST.get('x503')
        x504 = request.POST.get('x504')
        x505 = request.POST.get('x505')
        x506 = request.POST.get('x506')
        x507 = request.POST.get('x507')
        x508 = request.POST.get('x508')
        x509 = request.POST.get('x509')
        x510 = request.POST.get('x510')
        x511 = request.POST.get('x511')
        x512 = request.POST.get('x512')
        x513 = request.POST.get('x513')
        x514 = request.POST.get('x514')
        x515 = request.POST.get('x515')
        x516 = request.POST.get('x516')
        x517 = request.POST.get('x517')
        x518 = request.POST.get('x518')
        x519 = request.POST.get('x519')
        x520 = request.POST.get('x520')
        x521 = request.POST.get('x521')
        x522 = request.POST.get('x522')
        x523 = request.POST.get('x523')
        x524 = request.POST.get('x524')
        x525 = request.POST.get('x525')
        x526 = request.POST.get('x526')
        x527 = request.POST.get('x527')
        x528 = request.POST.get('x528')
        x529 = request.POST.get('x529')
        x530 = request.POST.get('x530')
        x531 = request.POST.get('x531')
        x532 = request.POST.get('x532')
        x533 = request.POST.get('x533')
        x534 = request.POST.get('x534')
        x535 = request.POST.get('x535')
        x536 = request.POST.get('x536')
        x537 = request.POST.get('x537')
        x538 = request.POST.get('x538')
        x539 = request.POST.get('x539')
        x540 = request.POST.get('x540')
        x541 = request.POST.get('x541')
        x542 = request.POST.get('x542')
        x543 = request.POST.get('x543')
        x544 = request.POST.get('x544')
        x545 = request.POST.get('x545')
        x546 = request.POST.get('x546')
        x547 = request.POST.get('x547')
        x548 = request.POST.get('x548')
        x549 = request.POST.get('x549')
        x550 = request.POST.get('x550')
        x551 = request.POST.get('x551')
        x552 = request.POST.get('x552')
        x553 = request.POST.get('x553')
        x554 = request.POST.get('x554')
        x555 = request.POST.get('x555')
        x556 = request.POST.get('x556')
        x557 = request.POST.get('x557')
        x558 = request.POST.get('x558')
        x559 = request.POST.get('x559')
        x560 = request.POST.get('x560')
        x561 = request.POST.get('x561')
        x562 = request.POST.get('x562')
        x563 = request.POST.get('x563')
        x564 = request.POST.get('x564')
        x565 = request.POST.get('x565')
        x566 = request.POST.get('x566')
        x567 = request.POST.get('x567')
        x568 = request.POST.get('x568')
        x569 = request.POST.get('x569')
        x570 = request.POST.get('x570')
        x571 = request.POST.get('x571')
        x572 = request.POST.get('x572')
        x580 = request.POST.get('x580')
        x581 = request.POST.get('x581')
        male = f"""I was born on the {x1} in {x2}, a city in {x3} at {x4} hospital.
            My full name is {x5} .

            The people who decided on this name are {x6}.
            I was named this way because {x7}.Sometimes, I go by the nickname {x8} which I got from {x9}.
            I have a beautiful mother named {x10}. She was born on {x11} in {x12}.
            The place she grew up in {x13} was lovely just like her.
            Meanwhile, my father, {x14}, was born on the {x15}. He was raised in
            the city of {x16}.


            To complete my family, I have {x17} siblings.
            Their names are {x18}. They were born in {x19}. My mother gave birth
            to {20} on {x21}. On the other hand,
            {x22} was born on {x23}.
            I have a beautiful/handsome sister/brother who goes by the name {x24}. She/he was born on the
            {x25} in
            {x26}.
            My mother was raised well by her parents, {x7} and {x27}. My
            grandmother was named {x28}. Her birthday was on
            the {x29}; whereas, my grandpa, {x30}, was born on {x31} in the village of {x32}.


            On my father???s side, I was blessed with the lives of my grandma, {x33}, and my grandpa, {x34}.
            Granny was born on {x35} in {x36}. My grandfather???s birth date,
            however, was on {x37}. His family
            gleefully welcomed him on this day in the city of {x38}.



            I have the most gorgeous wife. She was named {x39} but I call her {x40}. I am thankful that she was successfully given
            birth to on the{x41} in the wonderful city of {x42}.

            {x43} and I were blessed with {x44} children who we named as {x45}.
            {x46} was born on {x47} in {x48}. On the
            other hand, {x49}???s birthdate is on {x50}. My wife gave
            birth to him/her in {x51}.



            Over the years, my children grew up and had their own kids, too. My adorable grandkids are named {x580} and {x581}.
            The first one is born in {x52} on the {x53}.
            {x54} was born on {x55} in the city of {x55}.



            I spend most of my free time {x56} while drinking {x57}.


            My most favorite sport is {x58} because I think it is {x59}


            My go-to vacation spot is {x61}. I find it {x62}.


            The meal that I enjoy the most is {x63}.


            My favorite song is called {x64}; it is sung by {x65}. The reason why
            I love it is that it reminds me of
            {x67}.


            Currently, my favorite television show is {x68}. Back then, I really loved the series {x69}.



            I have watched the movie {x70} several times already and I never get tired of it because it is
            {x71}.


            My hobbies are {x72}, {x73}, and {x74}. On
            the weekends, I also {x75} with my {x76}.



            The social gatherings that I usually enjoy are {x77}.


            My greatest talent is {x78}. I have used it in many ways throughout my life such as when I
            {x79}.


            The best characteristic that I love about myself is my {x80}.

            Sometimes, I wish I could stop being {x81}.



            Currently, I am living a {x81} life here in {x82} with my {x83}.
            On the weekdays, I spend most of my time {x84}. By the end of the day, I would feel {x85} and {x86}.



            I grew up in a {x87} neighborhood where I met various interesting people like {x88}.
            Remembering it, I can say that it was actually a {x89} place.


            My childhood home was {x90}. I enjoyed all of the {x91} mornings and
            {x92} nights in it. The house was
            suitable for a family of {x93} people. My time there was {x94}.



            My favorite place in this {x95} house was the {x96}. It had a special
            place in my heart because it {x97}.




            When I was younger, I had to do chores like {x98}.


            ({x99}) I got a daily/weekly/monthly allowance worth {x100}.



            The indoor activity that I enjoyed the most was {x101}. This was because {x102}.


            Back then, I really enjoyed {x103} outside the house.


            As a child, I was particularly skilled at {x104}.



            I also had some toys that cheered me up on sad days. These are {x105}.



            I had a special place that I called ???mine.??? It was this {x106} space filled with {x107}. I used to {x108} a lot when
            I stayed here.


            As a child, I always anticipated going out to {x109}.



            Being a boy, I {x110} not enjoy reading.
            (If yes) I liked collecting {x111} books!


            of this experience???{x112}
            I lived in a {x113} (Religious/Non-Religious) family.
            (If religious). I attended a church called {x114} which was located in {x115}. I remember the times when I {x116}.

            I {x117} baptized or dedicated as an infant.
            (If baptized) As an infant, I was baptized by {x118} in {x119}. My
            {x120} attended the celebration



            Some of the childhood experiences that helped me become who I am right now are {x121}.



            I remember having a childhood friend named {x122}. He/she was very {x123} and we had a {x124} time together.



            From my childhood, I will be eternally grateful for the {x125}. Because of it, I grew up to be
            a {x126} person.
            Family LIFE
            50 A family is a circle of love?????formed by memories,??filled with devotion.????



            My favorite memory with my dad was when {x127}. This is a special event for me because {x128}.



            My father???s insights on life and its adventures was {x129}. This made me become more {x130} regarding my own life.


            My father and I used to {x131} together and I really enjoyed it because {x132}.


            I think I have grown up to be like my father when it comes to my {x133}. I always think that I
            got this from him.


            One thing my dad always said was {x134}. I believe that this is actually a great {x135} and it helped me
            establish myself.


            My father worked as a/an {x136}. This job piqued / did not pique my interest because {x137}.


            One of the most memorable things about my mother from when I was a little boy was how she {x138}. This is because {x139}.

            My mom always had a {x140} outlook towards life. This attitude of hers affected me in a way
            that I became more {x141}.



            I am similar to her because she is {x142} just like me. My mother is the most {x143} woman I have ever met and I love her
            for it.


            Back when I was a child, I really liked {x144} with my mom. Until now, I still feel {x145} whenever I remember this.




            My mother???s occupation was {x146}. This helped me decide on my future career because I found it
            {x147} how she
            {x148}.


            My family was {x149}. We encountered problems such as {x150} and it
            was hard for me growing up. But
            I am now {x151} about my life. These circumstances have made me {x152}
            and {x153}.

            As I was growing up, my parents requested that I {x154}.


            This formed my mindset regarding parenting. In complete honesty, I actually require my children to {x155}, similar to /
            different from the obligations I had as a kid.


            Some of the qualities that my parents nurtured in me are my characteristics of being {x156} and
            {x157}. I am thankful for these.



            My parents always told me to be a {x158} person. Of course, I valued their encouragement
            because I loved them.



            I also loved my siblings/sister/brother so much. My fondest memories of them/him/her was that time when {x159}.

            Of course, being young means you get to enjoy the beauty of life without heavily thinking of the consequences. I played
            around with my
            siblings/brother/sister and we used to {x160}. It was funny for me back then but looking back,
            I think {x161}.
            My siblings/brother/sister and I were {x162}. We had {x163} days
            together.
            In addition to our lovely family, we had a pet {x164} / pets named {x165}. He/she/they were adorable!
            The thing I loved most about having {x166} growing up with me was {x167}. I loved {x168} with {x169}!
            On regular days, my family {x170} together. In the summer, we would often go {x171}. But most especially,
            we loved spending time together, either by {x172} or {x173}.
            My early memories of my grandparents was how they {x174}. My grandma would always {x175} while my grandpa {x176}.

            They lived in a lovely place in {x177}. Around their area, there were many {x178}. It was a {x179} neighborhood.
            My grandmother worked as a {x180} and my grandpa did some {x181} job.

            Whenever my family visited them / whenever they visited us, I remember that we always had an amazing time together. My
            grandma and
            grandpa prepares a delicious meal for us. Their {x182} was my favorite!

            I loved being with my grandparents because they were {x183}. I always watched them {x184} . They cared for me and my
            siblings/brother/sister.
            A valuable lesson that I learned from being with them was that {x185}. Aside from this, I was
            also inspired by them to be a {x186}
            person.
            The only things I remember about my great-grandparents are that they {x187}.
            I believe that my ancestors were {x188} and that I might have a/an {x189} origin.
            My favorite home-cooked meal was {x190} because it was honestly delicious and {x191}! It reminds me of {x192}.
            Whenever my family and I {x193} together, we would always prepare {x194}.
            We used to go out for dinner frequently/sometimes. When we do, I would always request that we go to {x195} or try other restaurants
            that serve {x196}.
            (Yes) Our house was a great place for celebrations. I remember having company often. My family???s friends or some of our
            other relatives
            would always come to visit or {x197} with us.
            (No) Although we were a happy family, we did not often have company perhaps because our place was {x198}.
            My family outings were {x199}! We would always go to {x200} and {x201} together. Holidays are my {x202} favorite season!
            In the winter, I remember {x203} with my siblings/brother/sister. As a whole family, we liked
            playing {x204}. My favorite
            winter food was {x205}. And drinks? Of course, {x206}.
            Family reunions are {x207} for me. I enjoyed {x208} whenever we held
            one.
            (No) I was not really close to my relatives.
            (Yes) I had close relationships with my other relatives especially with my {x209}. I am happy
            about these because I could always
            {x210} to them whenever I am {x211}.

            Every time I think about my family, the first thing that comes to mind was {x212}. I feel like
            I associated them with it because of
            the {x213} they bring to my life.

            Knowledge is the power??that gives us wings to soar.??

            I attended elementary at {x214} in {x215}. I often rode the {x216} to school and back OR I often biked/walked to
            school alone/with my {x217}.My earliest memories of going to {x218} was that I would always {x219}
            in {x220} Class. I also remember hanging out
            with my childhood friends named {x221} and {x222}.
            92 WHAT DID YOU ENJOY?? MOST ABOUT ELEMENTARY SCHOOL?????
            One thing I loved most about elementary was {x223} on {x224} days.
            But, I really hated that I had to {x225}.
            Next, I attended middle school at {x226}. Every day, I would go there via {x227}. Sometimes, I would {x228}.
            When I was in high school, I attended {x229}. It was a very {x230}
            school and I met a lot of {x231} people there.
            My favorite subjects in middle school were {x232} and {x233} because
            {x234}.
            Meanwhile, in high school, I really liked going to {x235} class. The teacher was really {x236} and my classmates were
            {x237}.
            Some extracurricular activities that I enjoyed the most were {x238}. I chose these because
            {x239}.
            Over the years, I have received some special awards such as {x240}.
            I had a favorite teacher whose name was {x241}. I can say that she/he had a big influence on
            shaping who I am now by {x242}.
            Back when I was still in school, there were many fashion trends that arose such as {x243}.
            (Yes) I participated in them because {x244}.
            (No) I did not participate much when it comes to these because {x245}.
            The most popular songs that I remember around the time I was studying were {x246}. I really
            {x247} this kind of music.
            Meanwhile, the highest grossing movies were {x248}. People {x249}
            these so much!
            The television shows that were much awaited were {x250}.
            Lastly, celebrities such as {x251} were having their primes then.
            The parties that I attended were mostly {x252}. Some of the party-goers were from {x253}. I can still remember
            how {x254} the crowd was.
            (No) I didn???t have a car when I was in high school but if I did it probably would be a __________.
            (Yes) I had a car when I was a teenager and it was a {x255}. I was {x256} about how it looks like.
            I really went places with that car.
            My middle school and high school years were a bit difficult because of {x257}. But, as a whole
            I think I really {x258}
            my teenage years.
            DURING YOUR MIDDLE SCHOOL AND HIGH SCHOOL YEARS???
            I am happy that I got to {x259} while I was schooling. It was a great privilege for me.
            change with time?????
            During this time, I was thinking about my goal of becoming a {x260} and I really hoped to
            achieve my dreams such as
            that of {x261}. Over time, I continued/stopped inching towards these goals.
            After graduation, I chose to follow the path of becoming a {x262}.
            I went to college / a career training school called {x263} in the city of {x264}. I took up a degree in the field of
            {x265}.
            I had to move away from home to continue studying and it was {x266}. I was looking forward to
            {x267} but I really felt
            {x268} when I was away from my family.
            I lived in an apartment/dorm nearby. It was {x269}, {x270}, and {x271}. I had a {x272} time studying when I was
            there.
            (with roommate) I had a roommate whose name was {x273}. He/she was a {x274} person.
            My most favorite college memories were the one at {x275} with my {x276}. Those experiences were {x277}
            and unforgettable.
            On??the Job??

            Any job can be made great.??It???s the worker???not the work?????that counts

            When I was young, I tried to gain money by {x278}. My earnings were used to pay for my {x279}.


            My first career-oriented job after graduation was a {x280} at {x281}.
            Here, I would be the one responsible for
            {x282}.
            When I found out that I got accepted in this job, I was very {x283}. I thought that this can
            help me in {x284}.
            The one thing I love most about my first job was {x285}. The environment in the workplace was
            also {x286}.
            Among the jobs that I tried and had in the past, the one in which I probably had the most fun was when I was working at
            {x287}
            as a {x288}. This is due to the fact that {x289}.

            Meanwhile, the worst job was in {x290}. I mostly did not enjoy working here because of {x291}.
            The most rewarding out of all, however, was the job at {x292}. This is because I was {x293}. I really love
            {x294} about this job.
            Of course, some opportunities can only be achieved when you move out of your comfort zone. As for me, I had to move away
            when I
            was working at {x295} in {x296}. I felt {x297} because of it but I am {x298} that I took it.
            For some jobs, I had to go places for {x299} events. The most memorable place I visited while
            doing so was a {x300} in {x301}.
            I had a coworker / superior who displayed the role of a friendly and trustworthy mentor to me. His/her name was {x302} and
            he/she taught me how to {x303}.
            (If yes) Over the years, I was able to be a mentor to others, too. I believe it was a {x304}
            experience for me.
            (If no) I might not have been an official mentor to others myself, but I believe that I was also able to help my
            colleagues in various ways.

            At work, I met all types of people but I found {x305} friends, too.
            When I???m just at home, I like to work on {x306}.
            But, I usually avoid doing {x307} because {x308}.
            Love??AND??Marriage????
            130 When love touches our hearts,??happiness fills our days.??

            I remember having a crush on {x309} when I was younger. I believe she was the first person I
            truly admired.
            The first boy party that I attended was when I was {x310} years old. It was held at {x311}..
            My first kiss was {x312}. I remember how I felt really {x313}
            afterwards.
            My first ever date was {x314}. It went {x315}. I had a {x316} time with {x317}.
            When that happened, lovers usually {x318} when they went out together and hung out. The kind of
            date nights was very {x319}
            compared to now.
            I met my lovely wife when I was {x320} years old.


            I will be eternally grateful that our paths crossed on {x321} in {x322}. If it weren???t for the {x323},
            I wouldn???t have seen her.
            She was {x324}, {x325}, and {x326}. Those
            qualities really captured my attention.
            Initially, I thought that she was {x327}. Over time, I realized how {x328} my first impression was compared to how
            she really is.
            I courted her for {x329} months. She was definitely worth the wait.
            When we just started dating, we really loved {x330} together. Some other things that we enjoyed
            doing were {x331}
            and {x332}.
            I knew she was the one when {x333} after I realized that she could be {x334}.
            The marriage proposal was {x335} and I am sincerely {x336} about it!
            There were {x337} everywhere while I
            was waiting for her response.
            We officially tied the knot on {x338} at a {x339} in {x340}.


            I wore a {x341}.

            While she wore a beautiful and {x342} wedding dress/gown.??

            It was a small/big wedding. We had about {x343} guests.

            For our first dance as husband and wife, we swayed to the song entitled {x344} which was chosen
            because {x345}.
            The most remarkable memory of mine from that special day was {x346}.

            Recall a special moment or event from the honeymoon.??
            Our honeymoon was {x347}! We went to {x348} wherein we {x349}. What I loved most about this
            experience was the fact that {x350}.


            After getting married, we lived in {x351}. I clearly remember how {x352} our home was.


            Early into our marriage, we had {x353} nights where we would enjoy dinner together over a
            {x354}.
            We started thinking about having children when {x355}. I really looked forward to {x356} and seeing my wife
            {x357} for our kids.


            WHEN YOU WERE FIRST MARRIED???What were some of the fun things you did with them???
            As a couple, we had some close friends. The ones that we mostly hung out with were named {x358}.
            We would always {x359} together and it felt {x360}! I {x361} spending time with them.


            {x362} and I really loved {x363} whenever we had free time. Aside from
            this, we also enjoyed {x364}.
            For me, marriage has been rewarding because {x365}.
            To be able to withstand any hardship, I believe that the most important key to a healthy marriage is {x366}.
            Of course in our marriage we also had hard times wherein we needed to be there for each other more. These instances that
            required
            sharing and companionship happened when {x367}.
            My daily relationship with my loving wife has been {x368}. Right now, my favorite thing about
            being married to is {x369}.
            Parenting????
            To be a father is to protect,??nurture, and guide,??but most of all, to love.????


            When I found out that I was going to be a dad, I felt {x370}. I remember that day being a
            {x371}
            one.
            I lived in {x372}
            My FIRST CHILD WAS BORN on ??{x373}
            My growing family then lived at a {x374} in {x375}.


            Back then, our situation was {x376}.
            We had problems such as {x377} OR We did not have any problems.


            Every time I looked at my firstborn when he/she was an infant, I felt {x378}. Every day with
            him/her was really
            {x379}.


            Becoming a father was {x380}. It caused me to have a more {x381}
            outlook on life. I realized that {x382}.
            168 WHAT IS YOUR MOST VIVID MEMORY??OF YOUR CHILDREN???S EARLY YEARS?????
            I have some crystal clear memories of my children when they were still young. These include the time when {x383} and
            also that instance when {x384}.


            Back then, I really enjoyed {x386} with them. When they grew up a bit, we would always {x385}.
            Of course, there had to be some days that I would need to spend alone with my wife. Whenever we took the days off for
            our special dates,
            we would {x387}.

            As a parent, I believe that it is undeniable that I have similarities with my kids. These include {x388}.
            As for them, my kids are similar in a way that they are all {x389}. This might be because
            {x390}.
            My spouse and I tried to instill the qualities of being {x391}, {x392}, and {x393} to our kids.
            I know that I have been blessed to be a father because I get to experience {x394}. This is what
            I consider my greatest joy
            in this {x395} role.
            Because life is not perfect, our family had problems, too. The greatest challenge that I experienced as a dad to {x396} beautiful kids
            was {x397}.
            I was raised in a {x398} family which is similar/different to my children???s upbringing. They
            grew up in a {x399} house, a
            {x400} neighborhood, with {x401} parents.
            THAT YOU WISH YOU???D KNOWN WHEN YOU??FIRST BECAME A FATHER?????
            Sometimes, I wish that I knew better when I became a father to my firstborn. One thing that I learned through time that
            I could
            have known back when I was raising {x402} was {x403}.
            I am a {x404} person. Somehow I wish my kids can grow up to be {x405}
            -- opposite/similar to me.
            Being a father taught me a lot of {x406} lessons but to me the most important thing among all
            these is {x407}.
            This is due to the fact that {x408}.


            Life offers so many??wonderful things to share,??so many special joys to celebrate.????

            We would always {x409} on my birthday when I was young. The guests were usually {x410}. It was a {x411}
            celebration.


            My favorite memory of a birthday party was when {x412}. This happened on my {x413} th birthday.
            The most special presents that I ever received are {x414}. For me, they were wonderful because
            {x415}.
            I often requested that my parents cook/make/buy {x416} to serve on my birthdays. I really loved
            these food because
            {x417}.
            Apart from the celebration of my birth, I had other unique parties held at our humble abode. These include {x418}.
            The ambiance of the surroundings during this feast was {x419}. Guests had to wear {x420}.
            As a child, my favorite religious festivity is {x421}. We would {x422}
            together as a family and {x423}.
            We prepare meals such as {x424} to feast on.
            Among these types of celebrations, the main thing that stands out in my memory is {x425} due to
            the fact that
            {x426}.

            I really liked the {x427} that we buy/make during my childhood. It tasted {x428} and {x429}.
            My favorite christmas carol was {x420}. Right now, {x431} is my
            favorite.
            where??it??came??from?????
            What my family told us about Santa Claus was that he was/wasn???t real. I always knew/didn???t know where the gifts from my
            Christmas
            stocking / ornament came from.
            During these holidays, we often gave presents to each other. My most loved gift was the {x432}
            from my {x433}
            because {x434}.
            Meanwhile, the most memorable present that I gave someone was a {x435}. This was for my {x436}.
            I still remember how he/she {x437} it.
            Growing up, I always loved the religious tradition we had in our family. Now that I have my own, I continued to {x438}.
            As a parent, the most meaningful Christmas for me was when {x439} because {x440}.
            195 HOW DID YOU CELEBRATE THANKSGIVING???Did you have a favourite Thanksgiving tradition?????
            For Thanksgiving, my family usually {x441}. The tradition that I love most is {x442}.
            Preparing and eating Thanksgiving food is also {x443}.
            When I was a kid, I really {x444} Australia day. The neighborhood would always be {x445} and there were {x446}
            everywhere!
            What was your favourite Halloween treat?????
            I did/didn???t really enjoy halloween. I remember an especially fun costume worn by {x447}. It
            was a {x448}.
            I also {x449} to trick-or-treat! My favorite treat was {x450} since
            {x451}. One memory that I have of a really enjoyable holiday celebration was when {x452}. It happened around the time that {x453}. I think it was a meaningful experience for me because {x454}.
            Moment by moment,??day by day,??families create a lifetime of memories.??The happiest time of my life, I must say, is when {x455}. I cannot explain the joy that I felt because {x456}. To me, it???s an experience that cannot be beaten by anything else. Meanwhile, the saddest for me was when {x457}. I believe I had a {x458} time moving on from this
            because {x459}. Over the years, I had many commitments and responsibilities but there was a time wherein I was always occupied.
            The busiest I have ever been was when {x460}. It was due to the fact that {x461}. On the other hand, I had relaxing days, too, but I am confident to say that I was most comfortable and at ease when
            {x462}. A life-changing event that really influenced me in many ways was when {x463}. Somehow, it
            helped me {x464}. One political event that I participated in or witnessed over the years was {x465}. It made a
            really strong impression on for the reason that {x466}.  (I have) I served in the military back then. It was a {x467} experience, while at the same
            time, there were instances that {x468} me such as {x469}. (Other family members have) Some of my relatives had to serve in the military. I was really {x470} about it and it
            often {x471} me thinking about what was happening to them while in there.
            I can proudly say that I was able to {x472}. This had been fulfilling for me because {x473}.
            I have been in an accident/major surgery/long illness. This involved me being {x474}.
            It sincerely didn???t have / had a lasting effect on me because it made me {x475}.
            My family experienced a tragic time when {x476} happened. I have always been a {x477} person and although I was
            {x478}, I made sure that I would still be able to {x479}.
            YOU HAD TO MAKE IN YOUR LIFE???HAD TO MAKE IN YOUR LIFE???Would you make the same choice again?????
            The most difficult choice that I made was {x480}. I do not regret / regret it until now and if
            I would be given a chance to choose a different option, I would {x481}. Throughout the years, I really didn???t travel much / went to a lot of places but the most memorable experience I had
            while traveling was when I went to {x482} alone / with {x483}. There, I / we did
            activities such as {x484}. The first time I rode an airplane was when I was off to {x485} when I was {x486} years old. I had to go there because of
            {x487}. (No) I did not get the chance to travel abroad but I bet I would love to see {x488}.
            (Yes) I had the opportunity of traveling abroad and it was {x489}! I enjoyed {x490} because {x491}.
            Among all the tourist spots and vacation places that I have been to, I can say that the most interesting and exciting
            was when I went
            to {x492}. It was special because {x493}.
            I {x494} helping people because I believe that {x495}. One person that
            I extended my helping hands to was named {x496}.
            He/she needed assistance in {x497} so I {x498}.
            I also dedicated myself to a cause / organization for the {x499}. I participated in it with an
            open heart because {x500}.
            How did you benefit from it???
            I was also given the chance to join competitive activities like {x501} which helped me grow in
            a way that {x502}.
            Being on earth for {x503} years is a lot of work and over the years I did many {x504} things. Thankfully, my efforts were
            professionally recognized when I {x505}. Upon receiving my award, I felt {x506}.
            The most important invention in my lifetime was {x507}. I will be eternally grateful that it
            existed because
            {x508}.
            Some of the most remarkable political / international events that I witnessed or participated in while I am living were
            {x509}.
            These were memorable because {x510}.
            Science has always {x511} me but, in particular, {x512} piqued my
            interest.
            Growing up to be who I am today and comparing my upbringing to the youth of the current times, I can say that we are
            very
            similar / different in ways such as {x513}. This might be due to the fact that {x514} nowadays
            compared to back then.
            Even though I was {x515}, I don???t think I would want to change that about how I lived my life
            even if I would be given a chance to do
            so.
            Although, I guess I would have changed {x516} because {x517}.
            In the next ten years, I wish my family will become {x518} so that {x519}.
            For the world to be a better and happier place however, I hope that {x520} will change and
            {x521}
            can be more {x522}.
            Inspiration????How great it is??to have the freedom to dream??and the opportunity??to make those dreams come true.??

            The people I would like to thank for helping me be the person I am today are {x523}. They
            helped me
            {x524}.
            Whenever I needed help, I would always approach {x525} and he/she always had the answers that
            could make me {x526}.
            (No) Religion did not really play a significant role in my life.
            (Yes) Religion helped me be a {x527} person. I relied on my faith every time I {x528}.
            A poem/passage/quote that I learned to live by or admired sincerely was {x529} by {x530}. This is due to the fact that
            {x531}.
            If worst comes to worst and I am only allowed to keep a single family photo, it would be that of {x532}. This is {x533}
            for me because it reminds me of {x534}.
            Perhaps, the greatest possession that I have is my {x535}. It is unbeatable by any other
            because {x536}.
            The greatest gifts in my life are {x537}. I will forever be grateful for these.
            (No) I never felt that I was born to become someone.
            (Yes) I have always felt that I was born to be {x538} -- that I was called to {x539}.
            Back when I was little, I looked up to {x540} the most because {x541}.
            Somehow, I grew up to be
            closely similar to/different from them.
            A celebrity that I admired was {x542} because of his/her {x543}.
            If not, who would you like to hear and why?????
            (No) I have never been able to listen to a public speaker but if I would be given the chance, I want to hear {x544} because he/she
            {x545}.
            (Yes) I was able to witness {x546} speaking live and it greatly impacted me in a way that
            {x547}.

            What are some of the insights that you???ve received?????
            One book that has always made a big impression on me was {x548} by {x549}. I loved this author???s works because
            they taught me that {x550}.
            When I was young, I was told by {x551} that I should {x552}. They
            taught me this lesson
            when I was {x553}.
            To be able to work well with other people, one should be {x554}. It requires {x555} to build a lasting relationship.
            Success is something that {x556}. It does not {x557} and it is not
            {x558}.
            The secret to it would be {x559}. That is what I realized in my life on earth.
            CHARACTERISTICS OF A GOOD FRIEND?????
            One can only be considered a good friend if they are {x560}, {x561},
            and {x562}. If not, then there must be
            {x563}.
            What I value most about my family is the fact that {x564}. Even though there are hardships,
            we {x565} together.


            My life on earth has been emotionally {x566}, physically {x567}, and
            wholly {x568}. People have come
            and gone, seasons have changed countless times, and days have been numbered one by one. The single most important lesson
            I???ve learned in this {x569} world is that {x570}.
            The greatest advice I can give right now is that {x571}. I am hoping that people will listen and that my family will deem this as unforgettable and {x572}.
            PLEASE RECORD ANY OTHER INFORMATION YOU WISH TO SHARE """

        obj = Stroy(owner=request.user,
                    story_name='First Story', the_story=male)
        obj.save()
    return render(request, 'story/grandparent.html')