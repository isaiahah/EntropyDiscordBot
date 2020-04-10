module.exports = {
	name: 'vampireslash',
	description: 'Melee 1d7, apply 1d3 bleed.',
	execute(message, args) {
        var str;
        let absStr = parseInt(args[0].substr(1));
        if (args[0].startsWith("+")) {
            str = absStr;
        } else if (args[0].startsWith("-")) {
            str = (-1) * absStr;
        } else {
           str = 0;
        }
        var sphereResult1 = (Math.random() * 7) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var totalResult = diceResult1 + str;
        var sphereResult2 = (Math.random() * 3) + 1;
        var diceResult2 = Math.floor(sphereResult2);
        message.channel.send("Vampiric Slash 1d7 " + args[0] + " & 1d3 Bleed\nResults: " + diceResult1 + "\nTotal with Modifier: " + totalResult + "\nBleed: " + diceResult2)
	},
};