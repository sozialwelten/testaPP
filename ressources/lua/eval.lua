-- /// Custom Rules ///


-- /// Type Definitions ///

---@alias SequencePolicy
---|"required" If not matching or provided: breaks.
---|"allowed" If provided, has to match.
---|"optional" If not provided or not matching, will be replaced.
---|"accepted" If not matching, will be ignored.

---@alias FormatRule string|fun(string):boolean

---@class RuleBook
---@field policy SequencePolicy How to handle if not provided or not matching.
---@field tabus string|string[] Cannot be these literals.
---@field form FormatRule|FormatRule[] The form or pattern rules. strings for 'string.match(<sequence-part>, <arg>)' or a function that takes the sequence and returns a bool.
---@field length { [1]:integer, [2]:integer }|integer Can be specific length or { <min>, <max> }

---@class KeyGuard
---@field seq string[]
---@field rules table<string,RuleBook[]|string|string[]|nil>
---@field checks table<string,string|string[]> 'master' for global sentence check, or name of parts for partial check. Checks all strings in the array or single string. If one fails, will error or ignore rule and fallback to default.


-- /// Preset rule types ///
local R = {}

R.conditions = {
  hashtag = function(s)
    if not string.match(s, "#[%a_]+") then return false else return true end
  end,
  inscope = function(s, min, max)
    if #s > max then return false
    elseif #s < min then return false
    else return true end
  end
}


---@type KeyGuard[]
R.guards = {
  ---@type KeyGuard
  testakey = {
    checks = {
      _master = { "2025Z001-24c" }, Series = { "2025", "0000" }, UserToken = { "A", "B" }, Body = { "001", "000", "314" }, Suffix = { "-98ba7-99" }
    },
    seq = { "Series", "UserToken", "Body", "Suffix" },
    rules = {
      _master = "%d%d%d%d%w+%d%d%d[%-%d%w]*",
      Series = { policy = "required", tabus = {}, form = "%d+", length = 4 },
      UserToken = { policy = "required", tabus = {}, form = "%w+", length = { 1, 5 } },
      Body = { policy = "required", tabus = {}, form = "%d+", length = 3},
      Suffix = { policy = "optional", tabus = {}, form = "%-[%-%d%w]*[%d%w]" },
    },
  }
}


return R {}
