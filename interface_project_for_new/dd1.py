import  re
import unittest
def assertRegex(text, expected_regex, msg=None):
    """Fail the test unless the text matches the regular expression."""
    if isinstance(expected_regex, (str, bytes)):
        assert expected_regex, "expected_regex must not be empty."
        expected_regex = re.compile(expected_regex)
        #print("found")
        #return 3
    if not expected_regex.search(text):
        msg = msg or "Regex didn't match"
        msg = '%s: %r not found in %r' % (msg, expected_regex.pattern, text)
        #raise unittest.TestCase.failureException(msg)
        print(msg)
        return 4

    print ("found")
    return 1
response_to_check= {
    "fullname": "tester",
    "goods_type1": [
        {
            "goodsId": 1,
            "goods_name": "apple"
        },
        {
            "goodsId": 2,
            "goods_name": "apple"
        }
    ],
    "goods_type2": [
        {
            "goodsId": 1,
            "goods_name": "redapple"
        }
    ],
    "goods_type3": {
        "goodsId": 7
    },
    "goods_type4": 7,
    "price": {
        "apple": 10.5,
        "pear": 8
    }
}
response_to_check= str(response_to_check)
expected_result = {
"检查":"body",
"匹配规则":"匹配正则表达式",
"条件":[{"模式":"\'fullname111\': \'tester\'", "消息":"失败，success不为True"}]
}
for item in expected_result['条件']:
    pattern_str = item['模式']

    #logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
    a = assertRegex(response_to_check, pattern_str, msg=item['消息'])
    print(a)
