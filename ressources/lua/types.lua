---@alias FallbackType RulesTbl|fun():string|integer|nil|AllocTbl

---@class AllocTbl
---@field max* integer 
---@field min* integer Defaults to 1
---@field make fun(min*:integer,max*:integer,opts*:table):string|integer Generate function
---@field choices integer Defaults to 1. If more then one, user can choose

