# IMDb Builders

You can find items using the features of [IMDb.com](https://www.imdb.com/) (IMDb).

| Attribute                           | Description                                                                                                                                               | Works with Movies | Works with Shows | Works with Playlists and Custom Sort |
|:------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------:|:----------------:|:------------------------------------:|
| [`imdb_id`](#imdb-id)               | Gets the movie/show specified.                                                                                                                            |      &#9989;      |     &#9989;      |               &#10060;               |
| [`imdb_chart`](#imdb-chart)         | Gets every movie/show in an IMDb Chart like [IMDb Top 250 Movies](https://www.imdb.com/chart/top).                                                        |      &#9989;      |     &#9989;      |               &#9989;                |
| [`imdb_list`](#imdb-list)           | Gets every movie/show in an IMDb List, [IMDb Keyword Search](https://www.imdb.com/search/keyword/), or [IMDb Search](https://www.imdb.com/search/title/). |      &#9989;      |     &#9989;      |               &#9989;                |
| [`imdb_watchlist`](#imdb-watchlist) | Gets every movie/show in an IMDb User's Watchlist.                                                                                                        |      &#9989;      |     &#9989;      |               &#9989;                |

## IMDb ID

Gets the movie/show specified.

The expected input is an IMDb ID. Multiple values are supported as either a list or a comma-separated string.

```yaml
collections:
  Star Wars (Animated Shows):
    imdb_id: tt0458290, tt2930604
```

## IMDb Chart

Finds every item in an IMDb Chart.

The expected input are the options below. Multiple values are supported as either a list or a comma-separated string.

The `sync_mode: sync` and `collection_order: custom` Details are recommended since the lists are continuously updated and in a specific order.

| Name                                                                           | Attribute        | Works with Movies | Works with Shows |
|:-------------------------------------------------------------------------------|:-----------------|:-----------------:|:----------------:|
| [Box Office](https://www.imdb.com/chart/boxoffice)                             | `box_office`     |      &#9989;      |     &#10060;     |
| [Most Popular Movies](https://www.imdb.com/chart/moviemeter)                   | `popular_movies` |      &#9989;      |     &#10060;     |
| [Top 250 Movies](https://www.imdb.com/chart/top)                               | `top_movies`     |      &#9989;      |     &#10060;     |
| [Top Rated English Movies](https://www.imdb.com/chart/top-english-movies)      | `top_english`    |      &#9989;      |     &#10060;     |
| [Most Popular TV Shows](https://www.imdb.com/chart/tvmeter)                    | `popular_shows`  |     &#10060;      |     &#9989;      |
| [Top 250 TV Shows](https://www.imdb.com/chart/toptv)                           | `top_shows`      |     &#10060;      |     &#9989;      |
| [Top Rated Indian Movies](https://www.imdb.com/india/top-rated-indian-movies/) | `top_indian`     |      &#9989;      |     &#10060;     |
| [Lowest Rated Movies](https://www.imdb.com/chart/bottom)                       | `lowest_rated`   |      &#9989;      |     &#10060;     |

```yaml
collections:
  IMDb Top 250:
    imdb_chart: top_movies
    collection_order: custom
    sync_mode: sync
```

## IMDb List

Finds every item in an IMDb List or [Keyword Search](https://www.imdb.com/search/keyword/).

The expected input is an IMDb List URL or IMDb Keyword Search URL. Multiple values are supported as a list only a comma-separated string will not work.

The `sync_mode: sync` and `collection_order: custom` Details are recommended since the lists are continuously updated and in a specific order.

```yaml
collections:
  James Bonds:
    imdb_list: https://www.imdb.com/list/ls006405458
    collection_order: custom
    sync_mode: sync
```
```yaml
collections:
  IMDb Top 250:
    imdb_list: https://www.imdb.com/search/title/?groups=top_250
    collection_order: custom
    sync_mode: sync
```
```yaml
collections:
  Christmas:
    imdb_list:
      - https://www.imdb.com/list/ls025976544/
      - https://www.imdb.com/list/ls003863000/
      - https://www.imdb.com/list/ls027454200/
      - https://www.imdb.com/list/ls027886673/
      - https://www.imdb.com/list/ls097998599/
    sync_mode: sync
    collection_order: alpha
```

You can also limit the number of items to search for by using the `limit` and `url` parameters under `imdb_list`.

```yaml
collections:
  IMDb Popular:
    imdb_list:
      url: https://www.imdb.com/search/title/?title_type=feature,tv_movie,documentary,short
      limit: 50
    collection_order: custom
    sync_mode: sync
```

This can be used for multiple lists as seen below.

```yaml
collections:
  Top Action:
    imdb_list:
      - url: https://www.imdb.com/search/title/?title_type=feature&release_date=1990-01-01,&user_rating=5.0,10.0&num_votes=100000,&genres=action
        limit: 100
      - url: https://www.imdb.com/search/title/?title_type=feature&release_date=1990-01-01,&user_rating=5.0,10.0&num_votes=100000,&genres=action&sort=user_rating,desc
        limit: 100
```

You can also find episodes using `imdb_list` like so.

```yaml
collections:
  The Simpsons Top 100 Episodes:
    collection_order: custom
    builder_level: episode
    sync_mode: sync
    imdb_list:
      url: https://www.imdb.com/search/title/?series=tt0096697&sort=user_rating,desc
      limit: 100
    summary: The top 100 Simpsons episodes by IMDb user rating
```

## IMDb Watchlist

Finds every item in an IMDb User's Watchlist.

The expected input is an IMDb User ID (example: `ur12345678`). Multiple values are supported as a list or as a comma-separated string.

The `sync_mode: sync` and `collection_order: custom` Details are recommended since the lists are continuously updated and in a specific order.

```yaml
collections:
  My Watch Watchlist:
    imdb_watchlist: ur64054558
    collection_order: custom
    sync_mode: sync
```
```yaml
collections:
  My Friends Watchlists:
    imdb_watchlist: ur64054558, ur12345678
    collection_order: custom
    sync_mode: sync
```
```yaml
collections:
  My Friends Watchlists:
    imdb_watchlist: 
      - ur64054558
      - ur12345678
    collection_order: custom
    sync_mode: sync
```

## IMDb Search

Finds every item using an [IMDb Advance Title Search](https://www.imdb.com/search/title/)

The `sync_mode: sync` and `collection_order: custom` Details are recommended since the lists are continuously updated and in a specific order.

| Search Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `limit`            | Specify how items you want returned by the query.<br>**Options:** Any Integer greater then `0`<br>**Default:** `100`                                                                                                                                                                                                                                                                              |
| `sort_by`          | Choose from one of the many available sort options.<br>**Options:** `popularity.asc`, `popularity.desc`, `title.asc`, `title.desc`, `rating.asc`, `rating.desc`, `votes.asc`, `votes.desc`, `box_office.asc`, `box_office.desc`, `runtime.asc`, `runtime.desc`, `year.asc`, `year.desc`, `release.asc`, `release.desc`<br>**Default:** `popularity.asc`                                           |
| `title`            | Search by title name.<br>**Options:** Any String                                                                                                                                                                                                                                                                                                                                                  |
| `type`             | Item must match at least one given type. Can be a comma-separated list.<br>**Options:** `movie`, `tv_series`, `short`, `tv_episode`, `tv_mini_series`, `tv_movie`, `tv_special`, `tv_short`, `video_game`, `video`, `music_video`, `podcast_series`, `podcast_episode`                                                                                                                            |
| `type.not`         | Item must not match any of the given types. Can be a comma-separated list.<br>**Options:** `movie`, `tv_series`, `short`, `tv_episode`, `tv_mini_series`, `tv_movie`, `tv_special`, `tv_short`, `video_game`, `video`, `music_video`, `podcast_series`, `podcast_episode`                                                                                                                         |
| `release.after`    | Item must have been released after the given date.<br>**Options:** `today` or Date in the format `YYYY-MM-DD`                                                                                                                                                                                                                                                                                     |
| `release.before`   | Item must have been released before the given date.<br>**Options:** `today` or Date in the format `YYYY-MM-DD`                                                                                                                                                                                                                                                                                    |
| `rating.gte`       | Item must have an IMDb Rating greater then or equal to the given number.<br>**Options:** Any Number `0.1` - `10.0`<br>**Example:** `7.5`                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                
| `rating.lte`       | Item must have an IMDb Rating less then or equal to the given number.<br>**Options:** Any Number `0.1` - `10.0`<br>**Example:** `7.5`                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                
| `votes.gte`        | Item must have a Number of Votes greater then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                   |
| `votes.lte`        | Item must have a Number of Votes less then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                      |
| `genre`            | Item must match all genres given. Can be a comma-separated list.<br>**Options:** `action`, `adventure`, `animation`, `biography`, `comedy`, `documentary`, `drama`, `crime`, `family`, `history`, `news`, `short`, `western`, `sport`, `reality-tv`, `horror`, `fantasy`, `film-noir`, `music`, `romance`, `talk-show`, `thriller`, `war`, `sci-fi`, `musical`, `mystery`, `game-show`            |
| `genre.any`        | Item must match at least one given genre. Can be a comma-separated list.<br>**Options:** `action`, `adventure`, `animation`, `biography`, `comedy`, `documentary`, `drama`, `crime`, `family`, `history`, `news`, `short`, `western`, `sport`, `reality-tv`, `horror`, `fantasy`, `film-noir`, `music`, `romance`, `talk-show`, `thriller`, `war`, `sci-fi`, `musical`, `mystery`, `game-show`    |
| `genre.not`        | Item must not match any og the given genres. Can be a comma-separated list.<br>**Options:** `action`, `adventure`, `animation`, `biography`, `comedy`, `documentary`, `drama`, `crime`, `family`, `history`, `news`, `short`, `western`, `sport`, `reality-tv`, `horror`, `fantasy`, `film-noir`, `music`, `romance`, `talk-show`, `thriller`, `war`, `sci-fi`, `musical`, `mystery`, `game-show` |
| `event`            | Item must have been nominated for a category at the event given. Can be a comma-separated list.<br>**Options:** `cannes`, `choice`, `spirit`, `sundance`, `bafta`, `oscar`, `emmy`, `golden`, `oscar_picture`, `oscar_director`, `national_film_board_preserved`, `razzie`, or any [IMDb Event ID](https://www.imdb.com/event/all/) (ex. `ev0050888`)                                             |
| `event.winning`    | Item must have won a category at the event given. Can be a comma-separated list.<br>**Options:** `cannes`, `choice`, `spirit`, `sundance`, `bafta`, `oscar`, `emmy`, `golden`, `oscar_picture`, `oscar_director`, `national_film_board_preserved`, `razzie`, or any [IMDb Event ID](https://www.imdb.com/event/all/) (ex. `ev0050888`)                                                            |
| `imdb_top`         | Item must be in the top number of given Movies.<br>**Options:** Any Integer greater then `0`                                                                                                                                                                                                                                                                                                      |
| `imdb_bottom`      | Item must be in the bottom number of given Movies.<br>**Options:** Any Integer greater then `0`                                                                                                                                                                                                                                                                                                   |
| `company`          | Item must have been released by any company given. Can be a comma-separated list.<br>**Options:** `fox`, `dreamworks`, `mgm`, `paramount`, `sony`, `universal`, `disney`, `warner`, or any IMDb Company ID (ex. `co0023400`)                                                                                                                                                                      |
| `content_rating`   | Item must have the given content rating. Can be a list.<br>**Options:** Dictionary with two attributes `rating` and `region`<br>`rating`: Any String to match the content rating<br>`region`: [2 Digit ISO 3166 Country Code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)                                                                                                       |
| `country`          | Item must match with every given country. Can be a comma-separated list.<br>**Options:** [2 Digit ISO 3166 Country Code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)                                                                                                                                                                                                            |
| `country.any`      | Item must match at least one given country. Can be a comma-separated list.<br>**Options:** [2 Digit ISO 3166 Country Code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)                                                                                                                                                                                                          |
| `country.not`      | Item must not match any given country. Can be a comma-separated list.<br>**Options:** [2 Digit ISO 3166 Country Code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)                                                                                                                                                                                                               |
| `country.origin`   | Item must match any given country as the origin country. Can be a comma-separated list.<br>**Options:** [2 Digit ISO 3166 Country Code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)                                                                                                                                                                                             |
| `keyword`          | Item must match with every given keyword. Can be a comma-separated list.<br>**Options:** Any String                                                                                                                                                                                                                                                                                               |
| `keyword.any`      | Item must match at least one given keyword. Can be a comma-separated list.<br>**Options:** Any String                                                                                                                                                                                                                                                                                             |
| `keyword.not`      | Item must not match any given keyword. Can be a comma-separated list.<br>**Options:** Any String                                                                                                                                                                                                                                                                                                  |
| `series`           | Item must match with every given series. Can be a comma-separated list.<br>**Options:** Any IMDb ID (ex. `tt0096697`)                                                                                                                                                                                                                                                                             |
| `series.any`       | Item must match at least one given series. Can be a comma-separated list.<br>**Options:** Any IMDb ID (ex. `tt0096697`)                                                                                                                                                                                                                                                                           |
| `series.not`       | Item must not match any given series. Can be a comma-separated list.<br>**Options:** Any IMDb ID (ex. `tt0096697`)                                                                                                                                                                                                                                                                                |
| `list`             | Item must be on every given list. Can be a comma-separated list.<br>**Options:** Any IMDb List ID (ex. `ls000024621`)                                                                                                                                                                                                                                                                             |
| `list.any`         | Item must be on at least one given lists. Can be a comma-separated list.<br>**Options:** Any IMDb List ID (ex. `ls000024621`)                                                                                                                                                                                                                                                                     |
| `list.not`         | Item must not be on any given lists. Can be a comma-separated list.<br>**Options:** Any IMDb List ID (ex. `ls000024621`)                                                                                                                                                                                                                                                                          |
| `language`         | Item must match any given language. Can be a comma-separated list.<br>**Options:** [ISO 639-2 Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)                                                                                                                                                                                                                              |
| `language.any`     | Item must match at least one given language. Can be a comma-separated list.<br>**Options:** [ISO 639-2 Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)                                                                                                                                                                                                                     |
| `language.not`     | Item must not match any given language. Can be a comma-separated list.<br>**Options:** [ISO 639-2 Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)                                                                                                                                                                                                                          |
| `language.primary` | Item must match any given language as the primary language. Can be a comma-separated list.<br>**Options:** [ISO 639-2 Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)                                                                                                                                                                                                      |
| `popularity.gte`   | Item must have a Popularity greater then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                        |
| `popularity.lte`   | Item must have a Popularity less then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                           |
| `cast`             | Item must have all the given cast members. Can be a comma-separated list.<br>**Options:** Any IMDb Person ID (ex. `nm0000138`)                                                                                                                                                                                                                                                                    |  
| `cast.any`         | Item must have any of the given cast members. Can be a comma-separated list.<br>**Options:** Any IMDb Person ID (ex. `nm0000138`)                                                                                                                                                                                                                                                                 |  
| `cast.not`         | Item must not have any of the given cast members. Can be a comma-separated list.<br>**Options:** Any IMDb Person ID (ex. `nm0000138`)                                                                                                                                                                                                                                                             |  
| `runtime.gte`      | Item must have a Runtime greater then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                           |
| `runtime.lte`      | Item must have a Runtime less then or equal to the given number.<br>**Options:** Any Integer greater then `0`<br>**Example:** `1000`                                                                                                                                                                                                                                                              |
| `adult`            | Include adult titles in the search results.<br>**Options:** `true`/`false`                                                                                                                                                                                                                                                                                                                        |

### Examples

```yaml
collections:
  IMDb Popular:
    imdb_search:
      type: movie
      sort_by: popularity.asc
      limit: 50
    collection_order: custom
    sync_mode: sync
```

```yaml
collections:
  Top Action:
    imdb_search:
      type: movie
      release.after: 1990-01-01
      rating.gte: 5
      votes.gte: 100000
      genre: action
      sort_by: rating.desc
      limit: 100
```

You can also find episodes using `imdb_search` like so.

```yaml
collections:
  The Simpsons Top 100 Episodes:
    collection_order: custom
    builder_level: episode
    sync_mode: sync
    imdb_search:
      type: tv_episode
      series: tt0096697
      sort: rating.desc
      limit: 100
    summary: The top 100 Simpsons episodes by IMDb user rating
```
