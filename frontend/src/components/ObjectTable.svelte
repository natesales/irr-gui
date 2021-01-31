<script>
    import {Button, DataTable, Toolbar, ToolbarContent, Link} from "carbon-components-svelte";
    import Launch16 from "carbon-icons-svelte/lib/Launch16";
    import {onMount} from "svelte";

    let objects = [];

    onMount(() => {
        fetch("https://localhost/api/query", {
            method: "POST",
            body: JSON.stringify({
                "inverse": "origin",
                "value": "AS34553"
            })
        })
            .then(resp => resp.json())
            .then(data => {
                objects = data
                console.log(objects)
            })
    })
</script>

<main>
    <DataTable
            headers={[
                { key: "custom-primary-key", value: "Primary Key" },
                { key: "custom-object-type", value: "Type" },
                { key: "descr", value: "Description"},
                { key: "custom-maintainers", value: "Maintainers"},
                { key: "source", value: "Source"}
            ]}
            rows={objects}
            sortable
    >
<!--        <span slot="cell" let:row let:cell>-->
<!--            {#if cell.key === 'source' && cell.value === 'ARIN'}-->
<!--              <Link inline href="https://en.wikipedia.org/wiki/Round-robin_DNS" target="_blank"-->
<!--              >-->
<!--                {cell.value}-->
<!--                  <Launch16 />-->
<!--              </Link>-->
<!--            {:else}{cell.value}{/if}-->
<!--        </span>-->

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
