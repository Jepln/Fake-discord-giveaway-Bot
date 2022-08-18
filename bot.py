import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("token")
bot = commands.Bot(command_prefix="+", case_sensitive=False)
bot.remove_command("help")
@bot.event
async def on_ready():
     print("Bot logged in")

@bot.command()
@commands.has_permissions(administrator=True)
async def gw(ctx,winner:discord.Member,duration,*, msg):
      await ctx.message.delete()
      int_dur=int(duration)
      dur_mins=int_dur/60
      dur_hrs=dur_mins/60
      giveaway_embed=discord.Embed()
      giveaway_embed.title="Giveaway!!"
      giveaway_embed.description=f"""__{msg}__

      *Make sure to **react** with ⭐ to participate in this giveaway, ends in `{dur_hrs}` hours,* 
  
```Before participating we recommend you check if this giveaway has any requirements before entering.```

      """
      gw_msg=await ctx.send(embed=giveaway_embed)
      await gw_msg.add_reaction("⭐")
      await asyncio.sleep(int_dur)
      winner_embed=discord.Embed()
      winner_embed.title="Congratulations!!"
      winner_embed.description=f"<@{winner.id}> won `{msg}`"
      await ctx.send(f"Winner: <@{winner.id}>")
      await ctx.send(embed=winner_embed)
#use only 'seconds' in the while using the cmd, the time will be given in hrs in embed,
# example
# >giveaway @user(the winner) 18000(5.0 hrs, duration in seconds only) Nitro Classic (msg is the prize)


bot.run(TOKEN)