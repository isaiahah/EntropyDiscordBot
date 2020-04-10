module.exports = {
	name: 'longsword',
	description: 'Melee 2d5 + str',
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
        var sphereResult1 = (Math.random() * 5) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var sphereResult2 = (Math.random() * 5) + 1;
        var diceResult2 = Math.floor(sphereResult2);
        var totalResult = diceResult1 + diceResult2 + str;
        message.channel.send("Longsword 2d5 " + args[0] + "\nResults: " + diceResult1 + ", " + diceResult2 + "\nTotal with Modifier: " + totalResult)
	},
};