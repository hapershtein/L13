# Product Requirements Document

## 1. Introduction

This document outlines the product requirements for the CLI agent.

## 2. Goals

* To create a CLI agent that can call existing functions in a local project.
* To use the Gemini LLM to interpret natural language commands.
* To manage API keys securely.

## 3. Features

* **Function Calling:** The agent should be able to call functions from local Python files.
* **Natural Language Processing:** The agent should be able to understand natural language commands.
* **API Key Management:** The agent should load the Gemini API key from an environment file.
* **Extensibility:** The agent should be easily extensible with new functions.

## 4. Function List

* **get_local_time_and_date:** Returns the current local time and date.
* **get_upgradable_packages:** Returns a list of upgradable packages and their target versions.
* **get_geolocation:** Returns the user's geolocation based on their IP address.
