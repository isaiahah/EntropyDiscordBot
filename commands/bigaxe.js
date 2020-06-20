module.exports = {
	name: 'bigaxe',
	description: '2d10 + str',
	execute(message, args) {
        var str;
        let absstr = parseInt(args[0].substr(1));
        if (args[0].startsWith("+")) {
            str = absstr;
        } else if (args[0].startsWith("-")) {
            str = (-1) * absstr;
        } else {
            str = 0;
        }
        var sphereResult1 = (Math.random() * 10) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var sphereResult2 = (Math.random() * 10) + 1;
        var diceResult2 = Math.floor(sphereResult2);
        var totalResult = diceResult1 + diceResult2 + str;
        message.channel.send("Massive Axe 2d10 " + args[0] + "\nResults: " + diceResult1 + ", " + diceResult2 + "\nTotal with Modifier: " + totalResult)
	},
};