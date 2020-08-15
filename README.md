# WeatherBot  ![GitHub](https://img.shields.io/github/license/Austinwj/Project_Bot)



A Mastodon bot that can check weather conditions almost everywhere.

## Usage:

1. According to requirements.txt, ensure that there is an environment where the bot can run. If not, please run `pip3 install -r requirements.txt` in the WeatherBot installation directory.

2. Create a Mastodon account.

3. Log in to your Mastodon account and create a new application for the bot. The location is "Preferences"> "Development".

4. After clicking on the name you gave the robot, you can see a client ID, client secret and access token. 
   Please keep this important information.

5. Open `config.cfg`. Follow the instructions to add content:

   ```reStructuredText
   [WeatherBot]
   class = WeatherBot.ExampleBot
   domain = <your instance name here>
   client_id = <your client key here>
   client_secret = <your client secret here>
   access_token = <your access token here>
   ```

6. Run the `ananas` script: 
   `ananas -i exBot.cfg`

   * The script will ask for the email and password of your account on the Mastodon server

   * You only have to do this once, after that you can run the script as: 
     `ananas exBot.cfg`

## Explanation

* @WeatherBot can view instructions.
* The location can be input in multiple languages, Chinese and English are recommended. Among them, the Chinese input location query is the most accurate, because the location may have the same name, and the weather API used by the robot will optimize the ranking according to the frequency of location popularity when using Chinese input location for query.

See [ananas](https://github.com/chr-1x/ananas) for more details on the bot framework.

Learn more about [Mastodon](https://joinmastodon.org/#getting-started)

A [WeatherBot](https://uofgbot.top/about) example based on Mastodon instance, register and @[WeatherBot](https://uofgbot.top/about) for query!🤖