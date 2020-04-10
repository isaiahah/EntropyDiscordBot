module.exports = {
	name: 'elvenlamp',
	description: 'Heal 1d2',
	execute(message, args) {
        var sphereResult1 = (Math.random() * 2) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        message.channel.send("Elven Lamp 1d2 " + "\nResults: " + diceResult1)
	},
};