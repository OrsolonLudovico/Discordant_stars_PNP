# Discordant Stars — Print-and-Play Guide by a fan

A guide written aiming to simplyfy the process of printing a playable version of the the fan-made [Discordant
Stars](https://twilight-imperium.fandom.com/wiki/Discordant_Stars_Expansion_(UNOFFICIAL)) expansion for [Twilight Imperium: Fourth Edition](https://www.fantasyflightgames.com/productline/twilight-imperium-fourth-edition/).

## Premise and disclaimer

Discordant Stars is an **unofficial**, non-commercial **fan project**. It is not published, endorsed, sponsored, or otherwise affiliated with Asmodee, Fantasy Flight Games, or the creators of *Twilight Imperium*. *Twilight Imperium* and its associated names, logos, artwork, and intellectual property belong to their respective rights holders. The files and instructions in this repository are provided for personal, non-commercial use only. They must not be sold, bundled into a commercial product, or presented as official material. Please do not redistribute source files or artwork outside the channels and terms established by the original creators. Always check the current license, community guidelines, and distribution instructions supplied
with the source files before sharing or printing them. Futhermore this guide is made by an independent fan and it is not related to the actual creators of the expansion. Learn more on the dedicated [wiki](https://twilight-imperium.fandom.com/wiki/Discordant_Stars_Expansion_(UNOFFICIAL))

AI has been used to help for the creation of this project.

If you believe that material in this guide has been used improperly, or that a credit is missing, please contact me so it can be corrected.

## Table of Contents

[Before You Begin](#before-you-begin)
   [Introduction](#introduction)
   [Copyright and Community Disclaimer](#copyright-and-community-disclaimer)
[Use of Artificial Intelligence](#use-of-artificial-intelligence)
[Preparing the Files](#preparing-the-files)
   [Sources](#sources)
   [Uncharted Space](#uncharted-space)
   [Adapting the Files Using the Script](#adapting-the-files-using-the-script)
 [Printing](#printing)
   [Choosing the Materials](#choosing-the-materials)
   [Printing the Components](#printing-the-components)
   [Tools Needed](#tools-needed)

## Obtaining printable files

### Step 1: Download

The latest discordant files source files can be found in the [official Google drive folder](https://drive.google.com/drive/folders/1AipLLvGhyp2v--w2oeT7uQIovmH_HyVn).The most updated version of all the files will always be stored there. 

If you want you can directly download all the files (already converted into printable PDFs) from the [releases section](https://github.com/OrsolonLudovico/Discordant_stars_PNP/releases/) but THEY HAVE **SOME ISSUES**:
- The back of some cards is upside down with respect to the front (this doesn't affect gameplay but it's not the correct way to do it).

- Some assets are a little bit blurry (nothing too severe). 

- The faction sheets have some ugly angles.

You can learn how to prepare your own layout by reading this guide but if you choose to use those files you can jump directly to [Printing](#printing).

### Step 2: Fix the images

- Some images will be not vertical and they must be rotates, to do that **DO NOT** use *right click > rotate* because it will only apparently work, you need to rotate the actual pixels, you can use the [python script](Scripts/rotate.py) provided in this repo.

- In the drive images are provided in *PNG* which uses a relatively high amount of storage space and also often makes the application used to build the layout crash due to the large size. Converting to *jpg*/*jpeg* decreases the size of the files significantly enabling the layout application to crash considerably less, converting to *jpg*/*jpeg* (even with 100% quality) may still lead to a small increase in the image overall "blurryness". To convert a folder to *jpeg* in the correct way you can use the provided [python script](Scripts/convert%20to%20jpeg.py).

- Twilight Imperium cards are exactly $4.20 \times 6.40$ cm this means that the proportion is $ 4.2 \div 6.4 = \frac{21}{32}$. Some images are $\frac{1}{24} = 2 \times \frac{1}{48}$, to remove the excess $\frac{1}{24}$ from both sides you can uses the provided [python script](Scripts/tighten%201%20out%20of%2024.py).

### Step 3: Building the cards layout

To build the layout I used the [layout tool from pnpbuddy](https://pnpbuddy.com/layout/) which is a free online tool with no dowload or account requirement; this guide will use that website as reference.

#### 3.1 Uploading images

Just upload all the fronts and the backs in the dedicated sections, if you put the same number of fronts and backs the application will recognize that every front has a different back, if you put just one back the application will recognize that you want all the fronts to have the same back. You'll have a preview below the buttons. **WARINING** as mentioned before too many pictures or pictures that are too big may crash the application, try [converting to *JPEG*](#step-2-fix-the-images) or use less images at a time. 

<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
  <img src="assets/CardsLayout/UploadCardsUniq.png" alt="Example of uploading the cards with different backs" style="display: block; width: min(30%, 150px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
  <img src="assets/CardsLayout/uploadCardsSame.png" alt="Example of uploading the cards with the same back" style="display: block; width: min(30%, 150px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

#### 3.2 layout settings

Now you have to choose the settings:

- **PAPER SIZE** is whatever you want, A4 will be the easiest but it doesn't matter: the tool will automatically fit as much cars as it can in whatever size you choose (vertical and horizontal is also not important so do as you prefear).

- As mentioned before **CARD SIZE** is $4.20 \times 6.40$ cm so you should use *width = 42* and *heigt = 64*. If you're working on the faction sheets you should put they're measurements which are $19.00 \times 27.90$ cm, also experiment with the page orientation if you get an error.

- The **BLEED** is the amount of the images that should be outside the actual cards, in every image provided there is some bleed. For the cards in the [Uncharted Space folder](https://drive.google.com/drive/folders/1XAE7tO037fEPtYUDFTCLNXh8tp_fmXJU) and the faction sheets the bleed is *3mm* while for the rest of the cards the bleed is usually around *3.8mm* (the folders differ a bit). You should experiment, look at the results and figure out if the actual cards contain the images correctly.

- The **CROSSAIR** is teh guide that will help you cut the cards once printed, you can use the parameters that you prefear, be careful that if the crossair is too bug you risk for part of it to be left on the card once you do the cat. I used a *width* of 0.1 and a *Size* of 3 as in the picture

- The **BORDERS** should always be of *width 1*: they decide how much space there is between cards, you'll need a bit of space but too much and you're wasting paper. The radious is mostly fine at *3mm* (*Size "S"*) but **BE CAREFUL**, you need to remove the radious compleetly while woking on the faction sheets or you'll have ugly angles. The Color can be what you want but black helps if you miss-cut because it doesn't stick out usually.

<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/CardsLayout/LayoutSettings.png" alt="Examples of settings" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

After you adjusted the settings you can download the *PDF* by pressing the "Generate PDF" button

#### 3.3 Inspecting the PDF

Once you downloaded the PDF you should check that it has the correct real-world dimensions ($4.20 \times 6.40$ cm for standard cards, look at image) and also that the PDF is set to A4.

<div align="center">
  <img src="assets/CardsLayout/CardSize.png" alt="Actual size of action card" width="200">
</div>

Now check if the backs correspond to the fronts correctly. The image below shows the first two pages side by side; if, in a given row, the top left card of the first page is the front of the top right card on the same row of the second page the process was correct.
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/CardsLayout/PlanetsBack&Fronts.png" alt="Correct example of front and back" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

How should you rotate the images? The below example is what you should **NOT** do. Printing this way will results in the backs being upside down. In particular, if the images are horizontal, the front should have its bottom on the left while the top should have its bottom on the right **opposite to eachother**
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/CardsLayout/Mechs.png" alt="An example of ehat you should not do if you don't want your backs upside down" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

Now you're ready to print and cut your layouts, jump to the [printing section](#printing) if you don't need the exagon tiles and the tokens

### Step 4: Building the Hexagon layout
The hexagons need to be on tick cardboard and my solution was to print front and back on normal paper and then glue it on cardboard, so no more front and back on the same file.

To realize the exagons templates I used a websiste called [dextorous](https://www.dextrous.com.au/), it has some premium features but I didn't need them. I'll refear to that website for the next section. You need to create an account to start.

#### 4.1 Create the Layout
Go on *Layouts > new layout > start from empty layout*, press on the exagon and scroll down selecting an exagon. I choose "Hex 3.75 x 3.25 (95.3x82.6mm)" as a starting point but it shouldn't make a difference, now you should see an exagon on your screen
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/hexagon.png" alt="The exagon to press" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
   <img src="assets/HexagonLayout/Correcthexagon.png" alt="Press after scrolling down" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

The exagons of Twilight Imperium are regular exagons (all side has the same lenght) of side ***5.8cm***. This means that if you inscribe such an exagon in a quare you get a square of height 10.046cm (you can approximate to 10.05cm) and width 11.6cm. Let's put this measurements on the app: on the left panel press on positioning, scroll down until you see the measurements in pixels (px). Change the unit of measurements from "px" to "cm" and plug the measurements shown above. You should now have a regular exagon of the right size.
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/button.png" alt="Button" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
   <img src="assets/HexagonLayout/measurements.png" alt="Press after scrolling down" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

Now you need to position an image correctly so press on image (1) > look down and press the create a folder icon (2) to create a folder > open the folder > press the add image icon to add an image (3) > click on the image (4) > now the image will be floating in the center.
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/AddImage.png" alt="Procedure above" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

Now you'll need to play with the *custom size* slider and the *Image position* sliders to make the **front** of the image fit the exagon in the center (for the backs you'll need to make anouther layout exaclty the same as the first one but adjusting the image so that the exagon shows the back of the tile).

It should look something like this:
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/System.png" alt="Example of a system" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

#### 4.2 Populate the layout

Now we need to populate the layout with the actual fronts of the system tiles.

First tou'll need to add the system images to the folder yo've created before so go on Home > Images > select the folder > upload everything

To fill the layout you need a project: Home > Create a new peoject > create a new component > link the exagon layout you've created before, you should already have an exagon filled. Now press on the plus icon to spawn new exagons. From the table below change the image for each exagon until you have all the system tiles.
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/populate.png" alt="Example of a populated layout" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

#### 4.3 Export the Layout

From the previous screen press export and you'll see an export screen: on *Page setup* leave all as default amd press ecport. Now press Export > PDF - Chrome printer > be sure to follow the direction that the pop-up will give you > save as PDF.

Now you have a printable PDF, of course check the actual dimensions with a virtual ruler before printing, as you did in [a previous step](#33-inspecting-the-pdf)

### Step 5: Building the tokens Layout

I didn't bother printing every single faction-specific command and control token, it would be tedious and also expensive. I printed only the special tokens. To print them you'll need to build new layouts, most of them will be simply circles so you can use the circle preset.

Circle tokens dimensions are either 3.1cm or 1.8cm od diameter

Dimensions for the commodities increase tokens are in the image below
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/HexagonLayout/smallsig.png" alt="Commodities extra token size" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

## Printing and cutting

Here I will explain how to print and cut the printable PDF files obtained before, if you don't have printable PDFs you skipped too much, look [here](#obtaining-printable-files)

### How can I print them? Which materials should I use?

Printing the files at home is not the best if you don't have a professional printer. I went to a typography owned by a professional so I was able to ask some advice on the materials.

For the **tokens** and **system tiles** we choose 80g/m² lucid paper, scratch resistant. I glued them on 1cm tick cardboard I bought on Amazon, I needed 15 A4 sheets to create all the tiles.

For the **cards** and **faction sheets** I used 250g/m² paper. Paper with the same weight can have different elasticity levels, I recomand to test it personally againt original faction sheets and cards to select the best one aviable. Even the same type can have different charateristics depending on the lot so be careful and ask a professional. A good wat to start is checking if the height of the paper when put face down on a table is exactly the same as the height of an original card.

### Printing the Components

When printing print at 100% scale, real word measurements, do not press "fit to page". Messing up one setting will cause the backs and front to be misaligned

Pay attention to the colors, every printer prints differently so adjust the colors to match the references, I had to reduce all colors intensity by 20% and reduce the red one by 30% to achieve an acceptable result.


### Cutting the components

#### Tools Needed

- Angle cutter
- Big scissors
- Cutting Mat
- Glue
- Guilliotine paper cutter
- Hobby Knife
- Rulers

#### Cutting
- Cut the cars using the guilliotine, I do not advise to use one of those paper cutter with a slider (below under the "X"), they tend to suck and tear the paper. A guilliotine may seem less precise but after a couple of minutes cutting correctly will be easy and much faster. 
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/PrintAndcut/Papercutter.jpg" alt="Paper cutter" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>
You need to follow the guides on the agngles printed on the cards, evreything outside the area delined by the crosses will be discarted, that is the bleed. In the image you should cut over the dotted lines.
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: flex-start;">
   <img src="assets/PrintAndcut/cutDotted.png" alt="Cut over the dotted line" style="display: block; width: min(50%, 300px); max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.12);">
</div>

#### System tiles and tokens

For best results cut roughly the front of the system tiles and tokens and glue them with normal glue directly on the cardboard. After it dries cut the cardboard accurately with the scissors and you have the front.

For the backs: cut roughly the paper and glue it to the back of the corresponding piece of cardboard. After it dries turn the piece around and trim the edges with an hobby knife

#### Results

It is practically impossible to match the exact colors of the origial cards so a good strategy to hide the defects is to use sleeves. Twilight Imperium's card use 43 $\times$ 65mm sleeves (the cards are smaller but this is the size that fit best). I wasn't able to find non-transparent sleeves so I settled for the standars sapphire ones, which fit well enough and hide some defects.

Here include pictures of the actual results, for example compare action cards colors



////////////////////////////////////////////////

## Cover and box

Section under construction

## 3D printed insert

Section under construction

## Time and money spent for this porject

Section under construction

Time to build the files
Time to cut

Printing cost
Cardboard cost
Angle cutter cost
Sleeves cost
Box cost