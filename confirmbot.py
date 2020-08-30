import discord
from discord.ext import commands
import json
#the usual import lines
TOKEN = 'insert'#bottoken
client = commands.Bot(command_prefix = "notusedsowhocares")#making the bot itself

@client.event#the event
async def on_message(message=discord.Message):#the onmessage
    commandchannel = client.get_channel(745037746300780544)#this is our channel where you get the roles
    if message.channel == commandchannel: #checking if its the right channel


        memberrole = discord.utils.get(message.guild.roles, name="Member")#getting the member role
        rolesfile = open('roles.json', 'r')#opening our roles to letters list in read only (we only need to read)
        rolesdict = json.load(rolesfile) #making the rolesfile into a dict
        roleslist= []#the list of roles they will get that we append to
        if '100' in message.content:#seeing if it has 100 (applicant then)
            print('doing')#debugging
            applicantrole = discord.utils.get(message.guild.roles, name="Applicant")#getting the applicant role
            await message.author.add_roles(applicantrole,reason="ran command to get roles")#giving the norm roles
            await message.author.add_roles(memberrole,reason="ran command to get roles")#giving the norm roles
            roleslist.append("Applicant")#adding the applicant role to roleslist
            roleslist.append("Member")#adding the meber role to the roleslist
            for i in range(len(rolesdict)): #looping for the number of existant region roles
                cmdname = f"100{list(rolesdict.keys())[i]}"#the current command name it is looking for
                print(cmdname)#debugging purposes

                if cmdname in message.content or cmdname.lower() in message.content: #seeing if cmdname is what they are using
                    roleid = int(rolesdict[str(cmdname).lstrip("100")][1]) #grabbing the id
                    neededrole = message.guild.get_role(roleid)#grabbing the needed role to assign
                    await message.author.add_roles(neededrole)#adding that role
                    roleslist.append(neededrole.name)#appending region role to list
                    logchannel = client.get_channel(745039448898666516)#grabbing the log channel
                    await logchannel.send(f"{message.author.mention} has gotten roles {roleslist} from code \"{cmdname}\"") # sending the log message
        if '200' in message.content:#seeing if it has 200 (Builder then)
            print('doing')#debugging
            builderrole = discord.utils.get(message.guild.roles, name="Builder")#getting the builder role
            await message.author.add_roles(builderrole,reason="ran command to get roles")#giving the norm roles
            await message.author.add_roles(memberrole,reason="ran command to get roles")#giving the norm roles
            roleslist.append("Builder")#adding the builder role to roleslist
            roleslist.append("Member")#adding the meber role to the roleslist
            for i in range(len(rolesdict)): #looping for the number of existant region roles
                cmdname = f"200{list(rolesdict.keys())[i]}"#the current command name it is looking for
                print(cmdname)#debugging purposes

                if cmdname in message.content or cmdname.lower() in message.content: #seeing if cmdname is what they are using
                    roleid = int(rolesdict[str(cmdname).lstrip("200")][1]) #grabbing the id
                    neededrole = message.guild.get_role(roleid)#grabbing the needed role to assign
                    await message.author.add_roles(neededrole)#adding that role
                    roleslist.append(neededrole.name)#appending region role to list
                    logchannel = client.get_channel(745039448898666516)#grabbing the log channel
                    await logchannel.send(f"{message.author.mention} has gotten roles {roleslist} from code \"{cmdname}\"") # sending the log message

        await message.delete()
client.run(TOKEN)#running the bot
