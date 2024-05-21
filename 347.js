/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    if (nums.length === 0) {
        return 0
    }

    const dict = {}

    for (const num of nums) {
        if (dict[num] == null) {
            dict[num] = 0
        }
        dict[num] += 1
    }
    const keyPairs = Object.keys(dict).map((k) => {
        return [k, dict[k]]
    })
    const sortLs = keyPairs.sort((f, s) => {
        return s[1] - f[1]
    })
    
    console.log(sortLs.slice(0,k).map((a) => {return a[0]}));
};

topKFrequent([1,1,1,2,2,3,3,3,3,3,3],2)