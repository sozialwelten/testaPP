---@type testapp
local M = { config = {}, fn = {} }

M.config.instance = { timezone = "UTC" }

---@param method "force"|"update"|"break" How to handle if key is already existing.
---@param tbl1 table original table
---@param tbl2 table new values
---@return table result
function M.fn.merge_tables(method, tbl1, tbl2)
	local result = {}
	for key, val in pairs(tbl1) do
		result[key] = val
	end
	for key, val in pairs(tbl2) do
		if result.key and method == "break" then
			error(key .. " already has value", 1)
		elseif not result.key or method == "force" then
			result[key] = val
		end
	end
	return result
end

function M.setup(opts)
	M.config = M.fn.merge_tables("force", M.config, opts or {})
end

return M
