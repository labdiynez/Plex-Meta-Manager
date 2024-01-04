# Studio Collections

The `studio` Default Collection File is used to dynamically create collections based on the studios available in your library.

This file also merges similarly named studios (such as "20th Century Fox" and "20th Century Animation") into one ("20th Century Studios")

![](../images/studio.png)

## Requirements & Recommendations

Supported Library Types: Movie, Show

## Collections Section 070

| Collection                                           | Key                                                  | Description                                                                    |
|:-----------------------------------------------------|:-----------------------------------------------------|:-------------------------------------------------------------------------------|
| `Studio Collections`                                 | `separator`                                          | [Separator Collection](../separators.md) to denote the Section of Collections. |
| `<<Studio>>`<br>**Example:** `Blumhouse Productions` | `<<Studio>>`<br>**Example:** `Blumhouse Productions` | Collection of Movies/Shows that have this Studio.                              |

## Config

The below YAML in your config.yml will create the collections:

```yaml
libraries:
  Movies:
    collection_files:
      - pmm: studio
  TV Shows:
    collection_files:
      - pmm: studio
```

## Template Variables

Template Variables can be used to manipulate the file in various ways to slightly change how it works without having to make your own local copy.

Note that the `template_variables:` section only needs to be used if you do want to actually change how the defaults work. Any value not specified will use its default value if it has one if not it's just ignored.

??? info "Click to expand"

    === "File-Specific Template Variables"

        The below template variables are available specifically for this PMM Defaults file.

        Be sure to also check out the "Shared Template Variables" tab for additional variables.

        This file contains a [Separator](../separators.md) so all [Shared Separator Variables](../separators.md#shared-separator-variables) are available as well.

        | Variable                      | Description & Values                                                                                                                                                                                                                                            |
        |:------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | `limit`                       | **Description:** Changes the Builder Limit for all collections in a Defaults file.<br>**Values:** Number Greater than 0                                                                                                                                         |
        | `limit_<<key>>`<sup>1</sup>   | **Description:** Changes the Builder Limit of the specified key's collection.<br>**Default:** `limit`<br>**Values:** Number Greater than 0                                                                                                                      |
        | `sort_by`                     | **Description:** Changes the Smart Filter Sort for all collections in a Defaults file.<br>**Default:** `release.desc`<br>**Values:** [Any `smart_filter` Sort Option](../../files/builders/smart.md#sort-options)                                                     |
        | `sort_by_<<key>>`<sup>1</sup> | **Description:** Changes the Smart Filter Sort of the specified key's collection.<br>**Default:** `sort_by`<br>**Values:** [Any `smart_filter` Sort Option](../../files/builders/smart.md#sort-options)                                                               |
        | `include`                     | **Description:** Overrides the [default include list](#default-include).<br>**Values:** List of Studios found in your library                                                                                                                                   |
        | `exclude`                     | **Description:** Exclude these Studios from creating a Dynamic Collection.<br>**Values:** List of Studios found in your library                                                                                                                                 |
        | `addons`                      | **Description:** Overrides the [default addons dictionary](#default-addons). Defines how multiple keys can be combined under a parent key. The parent key doesn't have to already exist in Plex<br>**Values:** Dictionary List of Studios found in your library |
        | `append_include`              | **Description:** Appends to the [default include list](#default-include).<br>**Values:** List of Studios found in your library                                                                                                                                  |
        | `remove_include`              | **Description:** Removes from the [default include list](#default-include).<br>**Values:** List of Studios found in your library                                                                                                                                |
        | `append_addons`               | **Description:** Appends to the [default addons dictionary](#default-addons).<br>**Values:** Dictionary List of Studios found in your library                                                                                                                   |
        | `remove_addons`               | **Description:** Removes from the [default addons dictionary](#default-addons).<br>**Values:** Dictionary List of Studios found in your library                                                                                                                 |
        | `name_format`                 | **Description:** Changes the title format of the Dynamic Collections.<br>**Default:** `<<key_name>> <<library_translationU>>s`<br>**Values:** Any string with `<<key_name>>` in it.                                                                             |
        | `summary_format`              | **Description:** Changes the summary format of the Dynamic Collections.<br>**Default:** `<<library_translationU>>s that have the resolution <<key_name>>.`<br>**Values:** Any string.                                                                           |

        1. Each default collection has a `key` that when calling to effect a specific collection you must replace `<<key>>` with when calling.

    === "Shared Template Variables"

        {%
          include-markdown "../collection_variables.md"
        %}

    ### Example Template Variable Amendments

    The below is an example config.yml extract with some Template Variables added in to change how the file works.

    ???+ tip

        Anywhere you see this icon:
      
        > :fontawesome-solid-circle-plus:
      
        That's a tooltip, you can press them to get more information.

    ```yaml
    libraries:
      Movies:
        collection_files:
          - pmm: studio
            template_variables:
              append_include:
                - Big Bull Productions #(1)!
              sort_by: title.asc
              collection_mode: show_items #(2)!
              sep_style: gray #(3)!
    ```

    1.  add "Big Bull Productions" to the list of items that should be included in the Collection list
    2.  Show these collections and their items within the "Library" tab
    3.  Use the gray [Separator Style](../separators.md#separator-styles)

## Default values

??? tip

    These are lists provided for reference to show what values will be in use if you do no customization.  **These do not show how to change a name or a list.**

    If you want to customize these values, use the methods described above.

    **Default `include`**:

    ```yaml
    include:
    #### ANIMES ########################################################################################################
      - 8bit
      - A-1 Pictures
      - A.C.G.T.
      - Acca effe
      - Actas
      - AIC
      - Ajia-Do
      - Akatsuki
      - Animation Do
      - Ankama
      - APPP
      - Arms
      - Artland
      - Artmic
      - Arvo Animation
      - Asahi Production
      - Ashi Productions
      - asread.
      - AtelierPontdarc
      - B.CMAY PICTURES
      - Bandai Namco Pictures
      - Bee Train
      - Berlanti Productions
      - Bibury Animation Studios
      - bilibili
      - Bones
      - Brain's Base
      - Bridge
      - BUG FILMS
      - C-Station
      - C2C
      - Children's Playground Entertainment
      - Cloud Hearts
      - CloverWorks
      - Colored Pencil Animation
      - CoMix Wave Films
      - Connect
      - Craftar Studios
      - Creators in Pack
      - CygamesPictures
      - David Production
      - Diomedéa
      - DLE
      - Doga Kobo
      - domerica
      - Drive
      - EMT Squared
      - Encourage Films
      - ENGI
      - feel.
      - Felix Film
      - Fenz
      - GAINAX
      - Gallop
      - Geek Toys
      - Gekkou
      - Gemba
      - GENCO
      - Geno Studio
      - GoHands
      - Gonzo
      - Graphinica
      - Group Tac
      - Hal Film Maker
      - Haoliners Animation League
      - Hoods Entertainment
      - Hotline
      - J.C.Staff
      - Jumondou
      - Kadokawa
      - Khara
      - Kinema Citrus
      - Kyoto Animation
      - Lan Studio
      - LandQ Studio
      - Lay-duce
      - Lerche
      - LIDENFILMS
      - M.S.C
      - Madhouse
      - Magic Bus
      - Maho Film
      - Manglobe
      - MAPPA
      - Millepensee
      - Namu Animation
      - NAZ
      - Nexus
      - Nippon Animation
      - Nomad
      - Nut
      - Okuruto Noboru
      - OLM
      - Orange
      - Ordet
      - OZ
      - P.A. Works
      - P.I.C.S.
      - Passione
      - Pb Animation Co. Ltd
      - Pierrot
      - Pine Jam
      - Platinum Vision
      - Polygon Pictures
      - Pony Canyon
      - Production +h.
      - Production I.G
      - Production IMS
      - Production Reed
      - Project No.9
      - Quad
      - Radix
      - Revoroot
      - Saetta
      - SANZIGEN
      - Satelight
      - Science SARU
      - Sentai Filmworks
      - Seven Arcs
      - Shaft
      - Shin-Ei Animation
      - Shogakukan
      - Shuka
      - Signal.MD
      - Silver
      - SILVER LINK.
      - Square Enix
      - Staple Entertainment
      - Studio 3Hz
      - Studio A-CAT
      - Studio Bind
      - Studio Blanc.
      - Studio Chizu
      - Studio Comet
      - Studio Deen
      - Studio Elle
      - Studio Ghibli
      - Studio Flad
      - Studio Gokumi
      - Studio Guts
      - Studio Hibari
      - Studio Kafka
      - Studio Kai
      - Studio Mir
      - studio MOTHER
      - Studio Palette
      - Studio Rikka
      - Studio Signpost
      - Studio VOLN
      - STUDIO4°C
      - Sunrise Beyond
      - Sunrise
      - SynergySP
      - Tatsunoko Production
      - Telecom Animation Film
      - Tezuka Productions
      - TMS Entertainment
      - TNK
      - Toei Animation
      - Topcraft
      - Triangle Staff
      - Trigger
      - TROYCA
      - TYO Animations
      - Typhoon Graphics
      - ufotable
      - V1 Studio
      - W-Toon Studio
      - Wawayu Animation
      - White Fox
      - Wit Studio
      - Wolfsbane
      - Xebec
      - Yokohama Animation Lab
      - Yostar Pictures
      - Yumeta Company
      - Zero-G
      - Zexcs

    #### MOVIES & TV SHOWS ###############################################################################################
      - 3 Arts Entertainment
      - 6th & Idaho
      - 20th Century Animation
      - 20th Century Studios
      - 20th Century Fox Television
      - 21 Laps Entertainment
      - 87Eleven
      - 87North Productions
      - 101 Studios
      - 1492 Pictures
      - A Bigger Boat
      - A+E Studios
      - A24
      - Aardman
      - Aamir Khan Productions
      - ABC Signature
      - ABC Studios
      - Ace Entertainment
      - AGBO
      - Amazon Studios
      - Amblin Entertainment
      - AMC Studios
      - Anima Sola Productions
      - Annapurna Pictures
      - Ardustry Entertainment
      - Artisan Entertainment
      - Artists First
      - Atlas Entertainment
      - Atresmedia
      - Bad Hat Harry Productions
      - Bad Robot
      - Bad Wolf
      - Barunson E&A
      - Bakken Record
      - Bardel Entertainment
      - BBC Studios
      - Bill Melendez Productions
      - Blade
      - Bleecker Street
      - Blown Deadline Productions
      - Blue Ice Pictures
      - Blue Sky Studios
      - Bluegrass Films
      - Blueprint Pictures
      - Blumhouse Productions
      - Blur Studio
      - Bold Films
      - Bona Film Group
      - Bonanza Productions
      - Boo Pictures
      - Bosque Ranch Productions
      - Box to Box Films
      - Brandywine Productions
      - Broken Road Productions
      - Calt Production
      - Canal+
      - Carnival Films
      - Carolco
      - Cartoon Saloon
      - Carsey-Werner Company
      - Castle Rock Entertainment
      - CBS Productions
      - CBS Studios
      - CBS Television Studios
      - Centropolis Entertainment
      - Chernin Entertainment
      - Chimp Television
      - Chris Morgan Productions
      - Cinergi Pictures Entertainment
      - Columbia Pictures
      - Constantin Film
      - Cowboy Films
      - Cross Creek Pictures
      - Dark Horse Entertainment
      - Davis Entertainment
      - DC Comics
      - Dino De Laurentiis Company
      - Don Simpson Jerry Bruckheimer Films
      - Doozer
      - Dreams Salon Entertainment Culture
      - DreamWorks Studios
      - DreamWorks Pictures
      - Eleventh Hour Films
      - EMJAG Productions
      - Endeavor Content
      - Entertainment 360
      - Entertainment One
      - Eon Productions
      - Everest Entertainment
      - Expectation Entertainment
      - Exposure Labs
      - Fandango
      - Fields Entertainment
      - FilmDistrict
      - FilmNation Entertainment
      - Flynn Picture Company
      - Focus Features
      - Food Network
      - Fortiche Production
      - Fox Television Studios
      - Freckle Films
      - Frederator Studios
      - FremantleMedia
      - Fuqua Films
      - Gallagher Films Ltd
      - Gary Sanchez Productions
      - Gaumont
      - Generator Entertainment
      - Gracie Films
      - Green Hat Films
      - Grindstone Entertainment Group
      - Hallmark
      - HandMade Films
      - Happy Madison Productions
      - HartBeat Productions
      - Hartswood Films
      - Hasbro
      - HBO
      - Heyday Films
      - Hughes Entertainment
      - Hurwitz & Schlossberg Productions
      - Hyperobject Industries
      - Icon Entertainment International
      - IFC Films
      - Illumination Entertainment
      - Imagin
      - Imperative Entertainment
      - Impossible Factual
      - Ingenious Media
      - Irwin Entertainment
      - Jerry Bruckheimer Films
      - Jessie Films
      - Jinks-Cohen Company
      - Kazak Productions
      - Kennedy Miller Productions
      - Kilter Films
      - Kjam Media
      - Kudos
      - Kurtzman Orci
      - Laika Entertainment
      - Landscape Entertainment
      - Laura Ziskin Productions
      - Leftfield Pictures
      - Legendary Pictures
      - Let's Not Turn This Into a Whole Big Production
      - Lifetime
      - Levity Entertainment Group
      - Lightstorm Entertainment
      - Likely Story
      - Lionsgate
      - Live Entertainment
      - Lord Miller Productions
      - Lucasfilm Ltd
      - Magnolia Pictures
      - Malevolent Films
      - Mandalay Entertainment
      - Mandarin
      - Mandarin Motion Pictures Limited
      - Marv Films
      - Marvel Animation
      - Marvel Studios
      - Matt Tolmach Productions
      - Maximum Effort
      - Media Res
      - Metro-Goldwyn-Mayer
      - Michael Patrick King Productions
      - Millennium Films
      - Miramax
      - NEON
      - Netflix
      - New Line Cinema
      - Nickelodeon Animation Studio
      - NorthSouth Productions
      - Nu Boyana Film Studios
      - O2 Filmes
      - Open Road Films
      - Original Film
      - Orion Pictures
      - Palomar
      - Paramount Animation
      - Paramount Pictures
      - Paramount Television Studios
      - Participant
      - Phoenix Pictures
      - Piki Films
      - Pixar
      - Plan B Entertainment
      - PlayStation Productions
      - Playtone
      - Plum Pictures
      - Powerhouse Animation Studios
      - PRA
      - Prescience
      - Prospect Park
      - Pulse Films
      - Radar Pictures
      - RadicalMedia
      - Railsplitter Pictures
      - Rankin/Bass Productions
      - RatPac Entertainment
      - Red Dog Culture House
      - Regency Pictures
      - Reveille Productions
      - Rip Cord Productions
      - RocketScience
      - Savoy Pictures
      - Scenic Labs
      - Scion Films
      - Scott Free Productions
      - Sculptor Media
      - Sean Daniel Company
      - Secret Hideout
      - See-Saw Films
      - Serendipity Pictures
      - Show East
      - Showtime Networks
      - Sil-Metropole Organisation
      - Silverback Films
      - Siren Pictures
      - SISTER
      - Sixteen String Jack Productions
      - SKA Films
      - Sky studios
      - Skydance
      - Sony Pictures Animation
      - Sony Pictures
      - Sphère Média Plus
      - Spyglass Entertainment
      - Stöð 2
      - Star Thrower Entertainment
      - Stark Raving Black Productions
      - StudioCanal
      - Studio 8
      - Studio Babelsberg
      - Studio Dragon
      - STX Entertainment
      - Summit Entertainment
      - Syfy
      - Syncopy
      - T-Street Productions
      - Tall Ship Productions
      - Team Downey
      - Temple Street Productions
      - The Cat in the Hat Productions
      - The Donners' Company
      - The Jim Henson Company
      - The Kennedy-Marshall Company
      - The Linson Company
      - The Littlefield Company
      - The Mark Gordon Company
      - The Sea Change Project
      - The Weinstein Company
      - Tim Burton Productions
      - TOHO
      - Thunder Road
      - Titmouse
      - Tomorrow Studios
      - Touchstone Pictures
      - Touchstone Television
      - Trademark Films
      - Triage Entertainment
      - Tribeca Productions
      - TriStar Pictures
      - TSG Entertainment
      - Twisted Pictures
      - UCP
      - United Artists
      - Universal Animation Studios
      - Universal Pictures
      - Universal Television
      - Vancouver Media
      - Vertigo Entertainment
      - Village Roadshow Pictures
      - W. Chump and Sons
      - Walden Media
      - Walt Disney Animation Studios
      - Walt Disney Pictures
      - Walt Disney Productions
      - Warner Animation Group
      - Warner Bros. Pictures
      - Warner Bros. Television
      - Warner Premiere
      - warparty
      - Waverly Films
      - Wayfare Entertainment
      - Williams Street
      - Whitaker Entertainment
      - Wiedemann & Berg Television
      - Winkler Films
      - Wolf Entertainment
      - Working Title Films
    ```

    **Default `addons`**:

    ```yaml
    addons:
      8bit:
        - 8-bit
      20th Century Studios:
        - 20th Century
        - 20th Century Animation
        - 20th Century Fox
      AIC:
        - AIC ASTA
        - AIC A.S.T.A
        - AIC Build
        - AAIC PLUS+
        - AIC RIGHTS
        - AIC Spirits
      Ajia-Do:
        - Ajiado
      Amazon Studios:
        - Amazon
      Amblin Entertainment:
        - Amblin Television
      APPP:
        - A.P.P.P.
      asread.:
        - Asread
      AtelierPontdarc:
        - Atelier Pontdarc
      B.CMAY PICTURES:
        - G.CMay Animation & Film
      Bandai Namco Pictures:
        - Bandai Visual
        - Bandai Visual Company
      BBC Studios:
        - BBC
        - BBC Studios Natural History Unit
      Bibury Animation Studios:
        - Bibury Animation CG
      Blue Sky Studios:
        - Blue Sky Films
      Canal+:
        - Canal+ Polska
      Cloud Hearts:
        - CLOUDHEARTS
      Columbia Pictures:
        - Columbia TriStar
      CoMix Wave Films:
        - CoMix Wave
      Craftar Studios:
        - Craftar
      CygamesPictures:
        - Cygames Pictures
      DC Comics:
        - DC Films
        - DC Entertainment
      DreamWorks Studios:
        - DreamWorks
        - DreamWorks Animation
        - DreamWorks Animation Television
        - DreamWorks Classics
      EMT Squared:
        - EMT²0
      feel.:
        - Feel
      Gallop:
        - Studio Gallop
      Gaumont:
        - Gaumont International Television
      Geek Toys:
        - GEEKTOYS
      Gekkou:
        - GEKKOU Production
      GoHands:
        - Go Hands
      Gonzo:
        - Gonzo Digimation
      Hallmark:
        - Hallmark Channel
        - Hallmark Entertainment
        - Hallmark Media
        - Hallmark Movies & Mysteries
        - The Hallmark Channel
      Haoliners Animation League:
        - Haoliners Huimeng Animation
        - Haoliners Animation
      Illumination Entertainment:
        - Illumination Films
      J.C.Staff:
        - J.C. Staff
      Khara:
        - Studio Khara
      Lan Studio:
        - Studio LAN
      Legendary Pictures:
        - Legendary Television
      LIDENFILMS:
        - Liden Films
      Lucasfilm Ltd:
        - Lucasfilm
        - Lucasfilm Animation
      Mandarin:
        - Mandarin Films
        - Mandarin Television
      Marvel Studios:
        - Marvel Enterprises
        - Marvel Entertainment
        - Marvel
      Metro-Goldwyn-Mayer:
        - MGM
      New Line Cinema:
        - New Line
      Nexus:
        - Nexus Factory
      P.A. Works:
        - P.A.WORKS
      Paramount Pictures:
        - Paramount
      Pierrot:
        - Pierrot Plus
        - Studio Pierrot
      Pixar:
        - Pixar Animation Studios
      Plan B Entertainment:
        - PlanB Entertainment
      Platinum Vision:
        - PlatinumVision
      Production +h.:
        - Production +h
      Rankin/Bass Productions:
        - Videocraft International
      RatPac Entertainment:
        - Dune Entertainment
      Regency Pictures:
        - Regency Enterprises
        - New Regency Pictures
        - Monarchy Enterprises S.a.r.l.
      Science SARU:
        - Science Saru
      Seven Arcs:
        - Seven
        - Seven Arcs Pictures
      Shogakukan:
        - Shogakukan Production
      Signal.MD:
        - Signal MD
      Silver:
        - Studio Silver
      SILVER LINK.:
        - Silver Link
      Sky studios:
        - British Sky Broadcasting
        - British Sky Broadcasting(BSkyB)
      Skydance:
        - Skydance Media
      Sony Pictures:
        - Sony
        - Sony Pictures Animation
        - Sony Pictures Television Studios
      Studio Blanc.:
        - Studio Blanc
      Studio Deen:
        - Studio DEEN
      STX Entertainment:
        - STX Films
      The Kennedy-Marshall Company:
        - The Kennedy/Marshall Company
      The Mark Gordon Company:
        - Tiger Aspect Productions
      TOHO:
        - Toho Pictures
        - Toho Pictures, Inc.
      TMS Entertainment:
        - Tokyo Movie Shinsha
      Toei Animation:
        - Toei
      TriStar Pictures:
        - TriStar
      Universal Pictures:
        - Universal
        - Universal Animation Studios
      Walt Disney Pictures:
        - Disney
      Warner Animation Group:
        - Warner Bros. Cartoon Studios
        - Warner Animation
      Warner Bros. Pictures:
        - Warner
        - Warner Animation Group
      Yokohama Animation Lab:
        - Yokohama Animation Laboratory
    ```