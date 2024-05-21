/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    if (strs === null){
        return []
    }
    const dict = {}
    console.log(strs)

    for(const i in strs) {
        const key = strs[i].split("").sort().join("")
        if (dict[key] == null){
            dict[key] = []
        }
        dict[key] = [...dict[key], strs[i]]
    }

    const result = []

    for (const [key, value] of Object.entries(dict)){
        result.push(value)
    }
    
};

groupAnagrams(["eat","tea","tan","ate","nat","bat"])