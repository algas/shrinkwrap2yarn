# Migration shrinkwrap to yarn

Generate yarn.lock from npm-shrinkwrap.json.  
In spite of using shrinkwrap, we are suffered from dependency-hell of node packages.  
Throw away your [shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap) rally in [yarn](https://yarnpkg.com/).

## Repository

https://github.com/algas/shrinkwrap2yarn

## Environment

- Python 3.x
- node 4.x
- npm 3.x
- yarn 0.17.x

## Usage

Put the following commands in terminal.

1. Get source code  
`git clone https://github.com/algas/shrinkwrap2yarn.git && cd shrinkwrap2yarn`
2. Run shrinkwrap2yarn  
`python main.py /path/to/your_node_repo/npm-shrinkwrap.json > yarn.lock`
3. Delete your shrinkwrap  
`rm /path/to/your_node_repo/npm-shrinkwrap.json`
4. Install yarn  
`npm install -g yarn`
5. Install node dependencies  
`cd /path/to/your_node_repo && rm -r node_modules && yarn`

## Reference

- Migrating from npm  
https://yarnpkg.com/en/docs/migrating-from-npm
