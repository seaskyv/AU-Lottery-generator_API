# AU-Lottory-generator_API
Australian Lottery number generator, Powerball, Lotto and OZLotto.
This is the backend API component written in Python.

## Prerequisites
Python 3.7.2
Framework : Flask

## Setup

- Clone the repo and cd into the directory:

```
      $ git clone https://github.com/seaskyv/AU-Lottery-generator_API.git
      cd AU-Lottery-generator_API
```
- Install dependencies using pip:

```
      $ pip install pyyaml
      $ pip install Flask
```
- Start the service:
  
```
   $ python main.py
```

- Example call :
`http://localhost:9000/api?game=OZLotto&magic=1212&num=12&system=8`.
- Config file : `config.json`

## Contribute
Under the MIT License. 

#### Basic Git Workflow

- Clone the repo and cd into the directory:

```
      $ git clone https://github.com/seaskyv/AU-Lottery-generator_API.git
```

- Crfeate a branch for your fixes or new features:

```
      $ git checkout -b branch_name_here
```

- Make your update.

- Push to your fork Open a Pull Request!

## Related repository
```https://github.com/seaskyv/AU-Lottery-generator.git```
