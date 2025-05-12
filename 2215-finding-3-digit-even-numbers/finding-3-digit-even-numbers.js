/**
 * @param {number[]} digits
 * @return {number[]}
 */
var findEvenNumbers = function(digits) {
    const freq = new Array(10).fill(0);
    for (const digit of digits) {
        freq[digit]++;
    }

    const result = [];

    for (let num = 100; num <= 998; num += 2) {
        const hundreds = Math.floor(num / 100);
        const tens = Math.floor((num % 100) / 10);
        const units = num % 10;

        const tempFreq = new Array(10).fill(0);
        tempFreq[hundreds]++;
        tempFreq[tens]++;
        tempFreq[units]++;

        let isValid = true;
        for (let i = 0; i < 10; i++) {
            if (tempFreq[i] > freq[i]) {
                isValid = false;
                break;
            }
        }

        if (isValid) {
            result.push(num);
        }
    }

    return result;
}
