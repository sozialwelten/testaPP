---@class FediVerseInstance
---@field base_url? string Instace URL "https://<domain>.<top-level-domain>"
---@field name? string Instance Name. Defaults to "<domain>_<top-level-domain>"
---@field timezone? string Like "Europe/Berlin". Defaults to UTC.

---@class testappConfig
---@field instance? FediVerseInstance
---@field db? table

---@class testapp
---@field config? testappConfig
---@field setup? fun(opts: testappConfig):nil
