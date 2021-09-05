# Fotmob Api 
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A Python wrapper around the unofficial [FotMob](https://www.fotmob.com/) API
## Table of Contents

- [fotmob](#fotmob)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Install

```sh
pip install fotmob
```

## Usage

```python
from fotmob import Fotmob
fotmob = Fotmob()

fotmob.getMatchesByDate("20201020")
fotmob.getLeague("42", "overview", "league", "America/New_York")
fotmob.getTeam("6017", "overview", "team", "America/New_York")
fotmob.getPlayer("1071179")
fotmob.getMatchDetails("3399269")
```

## Contributing

Feel free to [open an issue](https://github.com/MatsAndT/fotmob/issues/new) or submit a pull request.

## License

[MIT](./LICENSE) © Mats Andreas Tønnesland