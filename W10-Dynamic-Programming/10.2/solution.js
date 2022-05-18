var countSubstrings = function (s) {
  let cnt = 0;
  for (let i = 0; i < s.length; i++) {
    for (let j = i; j < i + 2; j++) {
      let l = i;
      let r = j;
      while (l >= 0 && r < s.length && s[l] === s[r]) {
        cnt++;
        l--;
        r++;
      }
    }
  }
  return cnt;
};
