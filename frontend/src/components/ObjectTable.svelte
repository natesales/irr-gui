<script>
    import {Button, DataTable, Toolbar, ToolbarContent, Loading, ToolbarSearch} from "carbon-components-svelte";
    import {onMount} from "svelte";
    import {tab} from "../stores";

    let objects;
    let searchQuery;
    let filteredObjects = [];

    onMount(() => {
        fetch("/query", {
            method: "POST",
            body: JSON.stringify({
                "inverse": "origin",
                "value": "AS34553"
            })
        })
            .then(resp => resp.json())
            .then(data => {
                objects = data
                filteredObjects = data
            })
    })

    $: {
        if (objects && searchQuery) {
            filteredObjects = []; // Empty array
            for (const i in objects) {
                if (objects[i]["custom-primary-key"].includes(searchQuery)) {
                    filteredObjects.push(objects[i]);
                }
            }
        } else {
            filteredObjects = objects;
        }
    }
</script>

<main>
    {#if objects}
        <DataTable
                headers={[
                    { key: "custom-primary-key", value: "Primary Key" },
                    { key: "custom-object-type", value: "Type" },
                    { key: "descr", value: "Description"},
                    { key: "custom-maintainers", value: "Maintainers"},
                    { key: "source", value: "Source"}
                ]}
                bind:rows={filteredObjects}
                sortable
        >

            <span slot="cell" let:row let:cell>
                {#if cell.value === undefined}
                    None
                {:else}
                    {cell.value}
                {/if}
            </span>

            <Toolbar>
                <ToolbarContent>
                    <!--                TODO: Implement search -->
                    <ToolbarSearch bind:value={searchQuery}/>
                    <!--                <ToolbarMenu>-->
                    <!--                    <ToolbarMenuItem primaryFocus>Restart all</ToolbarMenuItem>-->
                    <!--                    <ToolbarMenuItem href="https://cloud.ibm.com/docs/loadbalancer-service">API documentation</ToolbarMenuItem>-->
                    <!--                    <ToolbarMenuItem danger>Stop all</ToolbarMenuItem>-->
                    <!--                </ToolbarMenu>-->
                    <Button on:click={() => {tab.set(1)}}>Create object</Button>
                </ToolbarContent>
            </Toolbar>
        </DataTable>
    {:else}
        <Loading/>
    {/if}
</main>
