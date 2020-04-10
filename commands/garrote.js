module.exports = {
	name: 'garrote',
	description: 'Melee 1d2 + str',
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
        var sphereResult1 = (Math.random() * 2) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var totalResult = diceResult1 + str;
        message.channel.send("Garrotte 1d2 " + args[0] + "\nResults: " + diceResult1 + "\nTotal with Modifier: " + totalResult)
	},
};