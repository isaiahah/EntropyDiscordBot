module.exports = {
	name: 'bad',
	description: 'BAD',
	execute(message, args) {
        message.delete()
        message.channel.send("NO")
	},
};