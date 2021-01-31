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
    } from "carbon-components-svelte";
</script>

<Form on:submit>
    <FormGroup>
        <Select id="select-1" labelText="Select menu" value="placeholder-item">
            <SelectItem
                    disabled
                    hidden
                    value="placeholder-item"
                    text="Choose an option"
            />
            <SelectItem value="route" text="route" />
            <SelectItem value="route6" text="route6" />
        </Select>
    </FormGroup>

    <FormGroup legendText="Checkboxes">
        <Checkbox id="checkbox-0" labelText="Checkbox Label" checked />
        <Checkbox id="checkbox-1" labelText="Checkbox Label" />
        <Checkbox id="checkbox-2" labelText="Checkbox Label" disabled />
    </FormGroup>
    <FormGroup legendText="Radio buttons">
        <RadioButtonGroup name="radio-button-group" selected="default-selected">
            <RadioButton
                    id="radio-1"
                    value="standard"
                    labelText="Standard Radio Button"
            />
            <RadioButton
                    id="radio-2"
                    value="default-selected"
                    labelText="Default Selected Radio Button"
            />
            <RadioButton
                    id="radio-4"
                    value="disabled"
                    labelText="Disabled Radio Button"
                    disabled
            />
        </RadioButtonGroup>
    </FormGroup>

    <Button type="submit">Submit</Button>
</Form>
