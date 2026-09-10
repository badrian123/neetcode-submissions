class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. If t is empty, there is nothing to search for.
        if t == "":
            return ""

        # 2. Count what characters t needs and how many of each.
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 3. Track how many character requirements are currently satisfied.
        have, need = 0, len(countT)

        # 4. Store the smallest valid window found.
        res, resLen = [-1, -1], float("infinity")

        # 5. Left pointer starts at the beginning of the window.
        l = 0

        # 6. Move the right pointer to expand the window.
        for r in range(len(s)):
            c = s[r]

            # 7. Add the new character into the current window count.
            window[c] = 1 + window.get(c, 0)

            # 8. If this character now has exactly enough copies,
            #    we satisfied one of t's requirements.
            if c in countT and window[c] == countT[c]:
                have += 1

            # 9. Once the window contains everything t requires,
            #    try shrinking it from the left.
            while have == need:

                # 10. Save this window if it is the smallest one found.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 11. Remove the leftmost character from the window.
                window[s[l]] -= 1

                # 12. If removing it causes us to no longer have enough
                #     of a required character, the window is no longer valid.
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # 13. Move the left pointer right to keep shrinking.
                l += 1

        # 14. Return the smallest valid window found.
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""