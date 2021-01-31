<script>
    import {Button, DataTable, Toolbar, ToolbarContent, ToolbarMenu, ToolbarMenuItem, ToolbarSearch} from "carbon-components-svelte";
</script>

<main>
    <DataTable
            headers={[{ key: "id", value: "Primary Key" }, { key: "type", value: "Type" }, { key: "descr", value: "Description"}, { key: "maintainers", value: "Maintainers"}, { key: "source", value: "RIR"}]}
            rows={[
                { id: "NATE", type: "mntner", descr: "Nathan Sales", maintainers: "NATE", source: "RIPE" },
                { id: "AS34553", type: "aut-num", descr: "Nathan Sales", maintainers: "NATE", source: "RIPE" },
                { id: "23.170.176.0/24", type: "route", descr: "", maintainers: "MNT-NS-787", source: "ARIN" }
            ]}
            sortable
    >

        <Toolbar>
            <ToolbarContent>
<!--                TODO: Implement search -->
<!--                <ToolbarSearch/>-->
<!--                <ToolbarMenu>-->
<!--                    <ToolbarMenuItem primaryFocus>Restart all</ToolbarMenuItem>-->
<!--                    <ToolbarMenuItem href="https://cloud.ibm.com/docs/loadbalancer-service">API documentation</ToolbarMenuItem>-->
<!--                    <ToolbarMenuItem danger>Stop all</ToolbarMenuItem>-->
<!--                </ToolbarMenu>-->
                <Button>Create object</Button>
            </ToolbarContent>
        </Toolbar>
    </DataTable>
</main>
