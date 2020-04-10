module.exports = {
	name: 'crossbow',
	description: '8 Range 1d10 + dex',
	execute(message, args) {
        var dex;
        let absDex = parseInt(args[0].substr(1));
        if (args[0].startsWith("+")) {
            dex = absDex;
        } else if (args[0].startsWith("-")) {
            dex = (-1) * absDex;
        } else {
           dex = 0;
        }
        var accuracySphere = (Math.random() * 20) + 1;
        var accuracyDie = Math.floor(accuracySphere);
        var totalAccuracy = accuracyDie + dex;
        var sphereResult1 = (Math.random() * 10) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var totalResult = diceResult1 + dex;
        message.channel.send("Crossbow 1d10 " + args[0] + "\nAccuracy: " + accuracyDie + args[0] + " = " + totalAccuracy + "\nResults: " + diceResult1 + "\nTotal with Modifier: " + totalResult)
	},
};