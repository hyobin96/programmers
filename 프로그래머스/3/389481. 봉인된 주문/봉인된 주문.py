def solution(n, bans):
    def get_word(n):
        total = 0
        r = 1
        while n > total:
            total += 26 ** r
            r += 1

        sub = total - 26 ** (r - 1)
        n -= sub

        gap = 26 ** (r - 2)
        words = []

        if n % (gap * 26) == 0:
            words.append('z' * (r - 1))
        else:
            for _ in range(r - 2):
                # ✅ float ceil 제거: 정수 올림 (n/gap의 ceil)
                k = (n + gap - 1) // gap  # 1..26
                if k == 26:
                    words.append('z')
                else:
                    words.append(chr(96 + k))

                n -= (k - 1) * gap
                gap //= 26

            if n == 0:
                words.append('z')
            else:
                words.append(chr(96 + n))

        return ''.join(words)

    word = get_word(n)

    # ✅ bans 중복 제거(중복 있으면 그만큼 n을 더 올려서 오답 가능)
    bans = sorted(set(bans), key=lambda b: (len(b), b))

    for ban in bans:
        if len(ban) < len(word):
            n += 1
        elif len(ban) == len(word) and ban <= word:
            n += 1
        word = get_word(n)

    return word
