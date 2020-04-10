module.exports = {
	name: 'longbow',
	description: '10 Range 2d3 + dex',
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
        var sphereResult1 = (Math.random() * 3) + 1;
        var diceResult1 = Math.floor(sphereResult1);
        var sphereResult2 = (Math.random() * 3) + 1;
        var diceResult2 = Math.floor(sphereResult2);
        var totalResult = diceResult1 + diceResult2 + dex;
        message.channel.send("Longbow 2d3 " + args[0] + "\nAccuracy: " + accuracyDie + args[0] + " = " + totalAccuracy + "\nResults: " + diceResult1 + ", " + diceResult2 + "\nTotal with Modifier: " + totalResult)
	},
};