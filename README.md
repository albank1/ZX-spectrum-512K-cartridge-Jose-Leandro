# ZX-spectrum-512K-cartridge-Jose-Leandro
512K ZX Spectrum multi cartridge
This is a 512KB cartridge that can hold 10 ROM games. The cartridge is currently supplied by MyRetro https://myretrostore.co.uk/ and the original creator was Jose Leandro https://trastero.speccy.org/cosas/JL/JL.htm
![Capture](https://github.com/user-attachments/assets/e0884ec6-c728-441e-8619-a445717cfdd5)

This is supplied with a ROM image compiled by the orginal creator.

I wanted to add my own game roms to this complilation so needed to know how to change the menu screen and  where to add the rom images.

The first Rom is stored at 04000h and the second at 08000h etc,
The menu is at 00500h and is in the format of a ZX Spectrum .SCR file. To create a new menu I saved the original, modified it with paint.
![New Menu1](https://github.com/user-attachments/assets/54e3479b-b245-4fa7-8a6f-752278cfedd0)

Next I use ZX Paintbrush https://sourcesolutions.itch.io/zx-paintbrush to convert it to a .SCR file.

To create the final ROM file I have just been using the software that came with the TL866 chip programmer, loading the orignal creators rom image, insert the .SCR into 00500h and then inserting the games roms into 04000h ect

