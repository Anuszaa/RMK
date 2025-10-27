import { MigrationInterface, QueryRunner, TableColumn } from "typeorm";

export class AddAccountDescription1623456789012 implements MigrationInterface {
    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.addColumn("account", new TableColumn({
            name: "description",
            type: "varchar",
            isNullable: true,
        }));
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropColumn("account", "description");
    }
}