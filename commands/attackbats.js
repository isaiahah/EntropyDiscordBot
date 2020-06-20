module.exports = {
	name: 'attackbats',
	description: '1d5 Bleed',
	execute(message, args) {
        var sphereResult1 = (Math.random() * 5) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        message.channel.send("Attack Bats 1d5 Bleed"+ "\nResults: " + diceResult1)
	},
};