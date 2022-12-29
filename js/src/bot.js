'use strict';

import {
  Client,
  CommandInteractionOptionResolver,
  GatewayIntentBits,
  SlashCommandStringOption,
  Routes,
} from 'discord.js';
import { config } from 'dotenv';
import { REST } from '@discordjs/rest';

config();

const client = new Client({
  intents: [
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.Guilds,
    GatewayIntentBits.MessageContent,
  ],
});

const rest = new REST({ version: '10' }).setToken(process.env.BOT_TOKEN);

client.on('ready', () => {
  console.log(`${client.user.tag} has logged in!`);
});

client.on('interactionCreate', interaction => {
  if (interaction.isChatInputCommand()) {
    console.log('chat_command');
    interaction.reply({ content: 'balls' });
  }
});

async function main() {
  const commands = [
    {
      name: 'memberlist',
      description: 'Show a list of server members',
    },
  ];
  try {
    console.log('Started refreshing application (/) commands.');
    await rest.put(
      Routes.applicationGuildCommands(
        process.env.CLIENT_ID,
        process.env.GUILD_ID
      ),
      {
        body: commands,
      }
    );
    client.login(process.env.BOT_TOKEN);
  } catch (err) {
    console.log(err);
  }
}

main();
