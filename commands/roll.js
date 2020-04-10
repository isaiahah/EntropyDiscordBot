module.exports = {
	name: 'roll',
	description: 'Roll Die with Modifier',
	execute(message, args) {
		if (args.length == 1) {
            let invalidDie = false;
            let diceSidesString = args[0].substr(1);
            var diceSidesInt = parseInt(diceSidesString);
            invalidDie = isNaN(diceSidesInt);
            var sphereResult = (Math.random() * diceSidesInt) + 1;
            var diceResult = Math.floor(sphereResult);
            if (invalidDie) {
                message.channel.send("Invalid Die");
            } else {
                message.channel.send("Rolling d" + diceSidesInt + "\nResult: " + diceResult);
            }
        } else if (args.length == 2) {
            let invalidDie = false;
            let invalidModifier = false;
            let diceSidesString = args[0].substr(1);
            var diceSidesInt = parseInt(diceSidesString);
            invalidDie = isNaN(diceSidesInt);
            let absRollModifier = parseInt(args[1].substr(1));
            var rollModifier;
            if (args[1].startsWith("+")) {
                rollModifier = absRollModifier;
            } else if (args[1].startsWith("-")) {
                rollModifier = (-1) * absRollModifier;
            } else {
                invalidModifier = true;
            }
            var sphereResult = (Math.random() * diceSidesInt) + 1;
            var diceResult = Math.floor(sphereResult);
            var modifiedResult = diceResult + rollModifier;
            if (invalidDie) {
                message.channel.send("Invalid Die");
            } else if (invalidModifier) {
                message.channel.send("Invalid Modifier");
            } else {
                message.channel.send("Rolling d" + diceSidesInt + "\nResult: " + diceResult + "\nWith Modifier: " + modifiedResult);
            }
        }
	},
};