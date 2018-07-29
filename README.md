# WoW Action Bars

The goal is to get similar spells bound to the same keys. This makes it easier to swap between characters.

### Preview HTML
https://dogbertai.github.io/wowactionbars/wowactionbars.htm

### How to read

Each class and spec has a column.

Each group of twelve is an action bar.

If you enable all 5 default action bars:

* AB1 - primary bar
* BL - bottom left bar
* BR - bottom right bar
* R1 - bar on right edge of screen
* R2 - next to R1
* S1-S3 - When you stealth as a rogue, or shapeshift as a druid, these are the bars that replace the primary bar

The 2nd column contains my keybinds. You can bind them to whatever you like.

The lowest cooldown, lowest priority spells are closer to the top of the spreadsheet (left in-game).

I use shift for all spells in the Bottom Left bar. I try to put all healing spells on this bar.

I use ctrl for all spells on the Bottom Right bar. I try to put important cooldowns on this bar.

Numbers next to spells are talents and their level.

H next to spells are PVP spells. This still needs work.

Orange spells are interchangeable across the talent row.

The bottom half can be ignored. It is just a way for me to categorize spells.

### Other notes

This doesn't show macros.

For me, all ally targeted spells are mouseover macroed.

Some summon spells are macroed to pet abilities when already summoned. e.g. Felhunter and Spell Lock.

Penance, Holy Shock, Intercept are slotted twice. One is a macro that only targets enemies. The other is a macro that only targets allies.

The class with the most abilities is Druid because of the forms. However, the stance bars make it easier to manage.

After the other bars are enabled, the primary bar has arrows to switch to yet one last bar (AB2). In there I have random stuff like archaelogy and professions.

If you use Bartender, I would put at least 3 action bars on top of each other corresponding to the first 3 bars.

I have auto attack on my bars because I play on a PVP server, and it's important to know if you're gonna attack someone with guards around.

### My bindings

    ctrl  F1 arena F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12
    shift F1 pet   F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12
    nomod F1 party F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12
    `          1 potion    2 extra  3 rez    4 br1   5 br4   6 br7
    ` setfocus 1 slow      2 trink  3 r24    4 heal  5 bl4   6 bl7
    ` focus    1 slow      2 r22    3 r25    4 ab1   5 ab4   6 inter
    Tab last   Q cc        W left   E right  R br2   T br5   Y br8      U        I     O        P
    Tab last   Q cure      W left   E right  R bl2   T bl5   Y bl8      U stats  I pvp O guild  P prof
    Tab assist Q dispel    W left   E right  R ab2   T aoe   Y taunt    U achiev I lfg O social P book
    Caps       A interact  S sound  D fps    F br3   G br6   H selfheal J        K         L
    Caps       A sheath    S opie   D opie   F bl3   G bl6   H bl9      J talent K         L guide
    Caps       A sit       S opie   D opie   F ab3   G ab6   H ab9      J char   K collect L quest
    Shift      Z petmove   X bag    C walk   V backward B land N racial M music , . nameplate / slash
    Shift      Z petfollow X bag    C follow V backward B fly  N move   M zone  , . nameplate / slash
    Shift      Z petattack X bag    C run    V backward B jump N speed  M map   , .           / slash
    Ctrl Alt Space forward MWUp zoomin     MWDn zoomout
    Ctrl Alt Space forward MWUp prevfriend MWDn nextfriend
    Ctrl Alt Space forward MWUp prevenemy  MWDn nextenemy
    M1 M2 M3 run M4 shift M5 ctrl M10 voice

* Ring finger is dedicated to strafe left.
* Middle finger is dedicated to strafe right.
* Thumb is used to run forward.
* I also roll the thumb so that I can press other buttons at the same time: autorun (C), back (V), jump (B), and speed (N).
* Almost all spells are activated by the index finger.
    * This allows all abilities to be activated while constantly moving in any direction.
* I use two mouse thumb buttons for Shift and Ctrl.

[OPie](https://wow.curseforge.com/projects/opie) is a radial action-binding addon. I use it for mage portals, raid markers, etc.

### How to use bindings

1. Make a copy of `C:\Program Files (x86)\World of Warcraft\WTF\Account\????\bindings-cache.wtf` and keep it in a safe place. (Exact path may vary.)
2. Replace it with my bindings-cache.wtf
3. Re-log into WoW.

### How to create the html

1. Create Excel spreadsheet with spells
2. Set the hyperlinks to wowhead spells
3. Save As Web Page
4. Publish: Sheet
5. Publish...
6. Save
7. Edit .htm file in text editor
8. Add these lines after `<meta>`

       <script>var whTooltips = {colorLinks: false, iconizeLinks: true, renameLinks: false, iconSize: 'medium'};</script>
       <script src="https://wow.zamimg.com/widgets/power.js"></script>
