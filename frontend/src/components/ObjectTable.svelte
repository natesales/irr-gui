<script>
    import {Button, DataTable, Toolbar, ToolbarContent, Loading, ToolbarSearch, ToolbarMenu, ToolbarMenuItem} from "carbon-components-svelte";
    import CheckmarkOutline20 from "carbon-icons-svelte/lib/CheckmarkOutline20";
    import MisuseOutline20 from "carbon-icons-svelte/lib/MisuseOutline20";
    import {onMount} from "svelte";
    import {tab} from "../stores";

    let objects;
    let searchQuery;
    let filteredObjects = [];
    let showRPKI = true;

    function fetchObjects(displayRPKI) {
        fetch("/query", {
            method: "POST",
            body: JSON.stringify({
                "inverse": "origin",
                "value": "AS34553"
            })
        })
            .then(resp => resp.json())
            .then(data => {
                let processedObjects = []
                for (const i in data) {
                    if(!data[i].source.includes("RPKI")) { // if not source RPKI
                        processedObjects.push(data[i])
                    } else if (displayRPKI) { // if RPKI source and we should display RPKI objects
                        console.log("showing", data[i].source)
                        processedObjects.push(data[i])
                    }
                }
                objects = processedObjects
                filteredObjects = processedObjects
            })
    }

    onMount(() => fetchObjects())
    $: fetchObjects(showRPKI)

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
                    <ToolbarSearch bind:value={searchQuery}/>
                    <ToolbarMenu>
                        <ToolbarMenuItem primaryFocus on:click={() => {showRPKI = !showRPKI}}>
                            {#if showRPKI}
                                <MisuseOutline20 />&nbsp;&nbsp;Hide RPKI
                            {:else}
                                <CheckmarkOutline20 />&nbsp;&nbsp;Show RPKI
                            {/if}
                        </ToolbarMenuItem>
                    </ToolbarMenu>
                    <Button on:click={() => {tab.set(1)}}>Create object</Button>
                </ToolbarContent>
            </Toolbar>
        </DataTable>
    {:else}
        <Loading/>
    {/if}
</main>
