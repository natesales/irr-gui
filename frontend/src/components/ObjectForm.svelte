<script>
    import {
        Form,
        FormGroup,
        Checkbox,
        RadioButtonGroup,
        RadioButton,
        Select,
        SelectItem,
        Button,
        TextArea,
        TextInput
    } from "carbon-components-svelte";

    let type = "route";
    let key;
    let database = "ALTDB";
    let generatedObject;
    let descr;

    $: {
        if (key) {
            generatedObject = type + ": " + key;
            if (descr) {
                generatedObject += "\ndescr: " + descr;
            }

            generatedObject += "\nsource: " + database;
        } else { // If primary key is empty, zero the object
            generatedObject = "";
        }
    }
</script>

<Form on:submit>
    <h2>Creating a new <u>{type}</u> object in <u>{database}</u></h2>
    <br>

    <FormGroup>
        <Select labelText="Object type" bind:selected={type}>
            <SelectItem value="route" text="route" />
            <SelectItem value="route6" text="route6" />
        </Select>

        <Select labelText="Database" value="placeholder-item" bind:selected={type}>
            <SelectItem value="ALTDB" text="ALTDB" />
            <SelectItem value="RIPE" text="RIPE" />
        </Select>
    </FormGroup>

    <FormGroup>
        <TextInput labelText="Primary Key" bind:value={key}/>
        <TextInput labelText="Description" bind:value={descr}/>
    </FormGroup>

    <FormGroup>
        <TextArea labelText="Generated Object" bind:value={generatedObject} />
    </FormGroup>

    <Button type="submit">Submit</Button>
</Form>
