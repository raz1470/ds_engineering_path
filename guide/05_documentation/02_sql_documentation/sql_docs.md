# SQL pipeline documentation
- [SQL pipeline documentation](#sql-pipeline-documentation)
  - [Introduction](#introduction)
  - [Mermaid](#mermaid)
  - [Execution sequence - Creating training and scoring data](#execution-sequence---creating-training-and-scoring-data)
  - [Table illustrations](#table-illustrations)
  - [Table illustration - playerbase](#table-illustration---playerbase)
  - [Table illustration - features\_01](#table-illustration---features_01)
  - [Table illustration - features\_02](#table-illustration---features_02)
  - [Table illustration - features\_03](#table-illustration---features_03)
  - [Table illustration - features\_04](#table-illustration---features_04)
  - [Table illustration - target](#table-illustration---target)
  - [Table illustration - scoring\_data](#table-illustration---scoring_data)
  - [Table illustration - trainig\_data](#table-illustration---trainig_data)

## Introduction
Documenting SQL scripts, execution sequences and resulting tables is important. This markdown file can be used as a template.


## Mermaid
Mermaid is a java script library for creating diagrams and flowcharts.

There are a number of extensions in VSC available to help create, view and export markdown files using Mermaid language:
- [Extension 1](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
- [Extension 2](https://marketplace.visualstudio.com/items?itemName=tomoyukim.vscode-mermaid-editor)
- [Extension 3](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.mermaid-export)
- [Extension 4](https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting )

For more details 


## Execution sequence - Creating training and scoring data
There is a crossover between the scripts used by the training and scoring DAGs.
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
flowchart TD
subgraph player_base
  playerbase[playerbase.sql]
end

subgraph features
  features_01[features_01.sql]
  features_02[features_02.sql]
  features_03[features_03.sql]
  features_04[features_04.sql]
end

subgraph target
  target.sql[target.sql.sql]
end

subgraph training
  training_data[training_data.sql]
end

subgraph scoring
  scoring_data[scoring_data.sql]
end

playerbase-->features
playerbase-->target
features-->scoring
features-->training
target-->training
```
## Table illustrations
|SQL filename|Output table|Author|Table summary|Primary key|
|-|-|-|-|-|
|playerbase.sql|playerbase|x|x|x|
|features_01.sql|features_01|x|x|x|
|features_02.sql|features_02|x|x|x|
|features_03.sql|features_03|x|x|x|
|features_04.sql|features_04|x|x|x|
|training_data.sql|training_data|x|x|x|
|scoring_data.sql|scoring_data|x|x|x|

## Table illustration - playerbase
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class playerbase

playerbase : column_01 (int)
playerbase : column_02 (date)
playerbase : column_03 (string)

playerbase <|-- raw_table_01
playerbase <|-- raw_table_02
playerbase <|-- raw_table_03
```

## Table illustration - features_01
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class features_01

features_01 : column_01 (int)
features_01 : column_02 (date)
features_01 : column_03 (string)

features_01 <|-- raw_table_01
features_01 <|-- raw_table_02
features_01 <|-- raw_table_03
```

## Table illustration - features_02
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class features_02

features_02 : column_01 (int)
features_02 : column_02 (date)
features_02 : column_03 (string)

features_02 <|-- raw_table_01
features_02 <|-- raw_table_02
features_02 <|-- raw_table_03
```

## Table illustration - features_03
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class features_03

features_03 : column_01 (int)
features_03 : column_02 (date)
features_03 : column_03 (string)

features_03 <|-- raw_table_01
features_03 <|-- raw_table_02
features_03 <|-- raw_table_03
```

## Table illustration - features_04
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class features_04

features_04 : column_01 (int)
features_04 : column_02 (date)
features_04 : column_03 (string)

features_04 <|-- raw_table_01
features_04 <|-- raw_table_02
features_04 <|-- raw_table_03
```

## Table illustration - target
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class target

target : column_01 (int)
target : column_02 (date)
target : column_03 (string)

target <|-- raw_table_01
target <|-- raw_table_02
target <|-- raw_table_03
```

## Table illustration - scoring_data
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class scoring_data

scoring_data : column_01 (int)
scoring_data : column_02 (date)
scoring_data : column_03 (string)

scoring_data <|-- raw_table_01
scoring_data <|-- raw_table_02
scoring_data <|-- raw_table_03
```

## Table illustration - trainig_data
```mermaid
%%{
  init: {
    'theme': 'default'
  }
}%%
classDiagram
class trainig_data

trainig_data : column_01 (int)
trainig_data : column_02 (date)
trainig_data : column_03 (string)

trainig_data <|-- raw_table_01
trainig_data <|-- raw_table_02
trainig_data <|-- raw_table_03
```